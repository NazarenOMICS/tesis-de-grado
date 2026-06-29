#Librerías
library(readxl)
library(dplyr)
library(ggplot2)
library(cowplot)

#Parámetros del experimento
PATH_TFOLD <- "C:/Users/Naza/Documents/Tesis de grado/Datos/Corrida 1 Triple STD/TFold_Analysis_ConParametrosAlejandro_2026-04-17.xlsx"
OUTPUT_PDF <- "Figure2B_replica.pdf"
OUTPUT_PNG <- "Figure2B_replica.png"

GT_HUMAN    <-  0
GT_BACTERIA <-  log2(20 / 10)
GT_YEAST    <-  log2(10 / 20)

ORG_COLORS <- c(
  "Human"    = "#CC44CC",
  "Yeast"    = "#228B22",
  "Bacteria" = "#DAA520"
)
#Cargar el Excel
sheets <- c("Blue Dots", "Green Dots", "Red Dots")
df_list <- lapply(sheets, function(s) {
  d <- read_excel(PATH_TFOLD, sheet = s)
  d$category <- s
  d
})
df <- bind_rows(df_list)

#Clasificar por organismo
df <- df %>%
  mutate(organism = case_when(
    grepl("Escherichia", Description)   ~ "Bacteria",
    grepl("Saccharomyces", Description) ~ "Yeast",
    grepl("Homo sapiens", Description)  ~ "Human",
    TRUE                                 ~ "Other"
  ))

#Calcular log2FC
df <- df %>%
  mutate(
    log2FC    = sign(`Fold Change`) * log2(abs(`Fold Change`)),
    log10_int = log10((`Signal(Bottom)` + `Signal(Top)`) / 2)
  )

#Limpieza de datos vacios
df <- df %>%
  filter(is.finite(log2FC), is.finite(log10_int))

#Normalización por mediana
median_correction <- median(df$log2FC)
cat("Corrección por mediana:", round(median_correction, 4), "\n")

df <- df %>%
  mutate(log2FC_med = log2FC - median_correction)

GT_HUMAN_med    <- GT_HUMAN    - median_correction
GT_BACTERIA_med <- GT_BACTERIA - median_correction
GT_YEAST_med    <- GT_YEAST    - median_correction

#Generacion del panel
make_panel <- function(data, y_col, gt_h, gt_b, gt_y, title, y_lim = c(-3.5, 3.5)) {
  
  data <- data %>% mutate(.y = .data[[y_col]])
  
  data <- data %>%
    mutate(org_order = factor(organism, levels = c("Human", "Yeast", "Bacteria"))) %>%
    arrange(org_order)
  
  ggplot(data, aes(x = log10_int, y = .y, color = organism)) +
    geom_density_2d(alpha = 0.15, linewidth = 0.3, bins = 10) +
    geom_point(alpha = 0.45, size = 1.2, shape = 16) +
    geom_hline(yintercept = gt_h, color = ORG_COLORS["Human"],    linewidth = 1.0) +
    geom_hline(yintercept = gt_b, color = ORG_COLORS["Bacteria"], linewidth = 1.0) +
    geom_hline(yintercept = gt_y, color = ORG_COLORS["Yeast"],    linewidth = 1.0) +
    scale_color_manual(
      values = ORG_COLORS,
      labels = c("Bacteria" = "Bacteria (E. coli)",
                 "Human"    = "Human",
                 "Yeast"    = "Yeast (S. cerevisiae)")
    ) +
    scale_y_continuous(limits = y_lim, breaks = seq(-3, 3, 1)) +
    labs(x = "log10 relative intensity", y = "log2FC", title = title, color = NULL) +
    theme_bw(base_size = 11) +
    theme(
      panel.grid.minor   = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_line(color = "grey90"),
      plot.title         = element_text(size = 11, face = "bold"),
      legend.position    = "bottom",
      legend.key.size    = unit(0.4, "cm")
    ) +
    guides(color = guide_legend(override.aes = list(size = 2.5, alpha = 1)))
}


#Elementos del panel
panel_no_norm <- make_panel(
  data = df, y_col = "log2FC",
  gt_h = GT_HUMAN, gt_b = GT_BACTERIA, gt_y = GT_YEAST,
  title = "No Post-processing norm."
)

panel_median <- make_panel(
  data = df, y_col = "log2FC_med",
  gt_h = GT_HUMAN_med, gt_b = GT_BACTERIA_med, gt_y = GT_YEAST_med,
  title = "+median norm."
)
legend_shared <- get_legend(panel_no_norm)

panels <- plot_grid(
  panel_no_norm + theme(legend.position = "none"),
  panel_median  + theme(legend.position = "none"),
  ncol = 2, align = "hv"
)

final_fig <- plot_grid(panels, legend_shared, ncol = 1, rel_heights = c(1, 0.08))

#Guardar imagenes
ggsave(OUTPUT_PDF, final_fig, width = 10, height = 5.5, device = cairo_pdf)
ggsave(OUTPUT_PNG, final_fig, width = 10, height = 5.5, dpi = 300)
