library(readxl)
library(dplyr)
library(ggplot2)
library(cowplot)

# --- PARÁMETROS -----------------------------------------------------------

PATH_PW  <- "C:/Users/Naza/Documents/Tesis de grado/Datos/Corrida 1 Triple STD/Pairwise_comparison_TripleSTD.xlsx"
OUT_PNG  <- "Pairwise_Figure2B_style.png"
OUT_PDF  <- "Pairwise_Figure2B_style.pdf"

GT_HUMAN    <-  0
GT_BACTERIA <-  log2(20 / 10)   # +1
GT_YEAST    <-  log2(10 / 20)   # -1

ORG_COLORS <- c(
  "Human"    = "#CC44CC",
  "Yeast"    = "#228B22",
  "Bacteria" = "#DAA520"
)

# --- CARGA Y PREPARACIÓN --------------------------------------------------

df <- read_excel(PATH_PW, sheet = "Table1")

df <- df %>%
  mutate(
    organism = case_when(
      grepl("Escherichia",   OS) ~ "Bacteria",
      grepl("Saccharomyces", OS) ~ "Yeast",
      grepl("Homo sapiens",  OS) ~ "Human",
      TRUE                        ~ "Other"
    ),
    log10_pep = log10(`PEPTIDE COUNT`)
  )

# Normalización por mediana (mismo criterio que TFold)
median_correction <- median(df$`LOG2(FOLD)`)
cat("Corrección por mediana:", round(median_correction, 4), "\n")

df <- df %>%
  mutate(log2FC_med = `LOG2(FOLD)` - median_correction)

GT_HUMAN_med    <- GT_HUMAN    - median_correction
GT_BACTERIA_med <- GT_BACTERIA - median_correction
GT_YEAST_med    <- GT_YEAST    - median_correction

# --- FUNCIÓN PANEL --------------------------------------------------------

make_panel <- function(data, y_col, gt_h, gt_b, gt_y, title, y_lim = c(-3.5, 3.5)) {
  
  data <- data %>%
    mutate(
      .y        = .data[[y_col]],
      org_order = factor(organism, levels = c("Human", "Yeast", "Bacteria"))
    ) %>%
    arrange(org_order)
  
  ggplot(data, aes(x = log10_pep, y = .y, color = organism)) +
    geom_hline(yintercept = gt_h, color = ORG_COLORS["Human"],    linewidth = 1.0) +
    geom_hline(yintercept = gt_b, color = ORG_COLORS["Bacteria"], linewidth = 1.0) +
    geom_hline(yintercept = gt_y, color = ORG_COLORS["Yeast"],    linewidth = 1.0) +
    geom_point(alpha = 0.75, size = 2.5, shape = 16) +
    scale_color_manual(
      values = ORG_COLORS,
      labels = c(
        "Bacteria" = "Bacteria (E. coli)",
        "Human"    = "Human",
        "Yeast"    = "Yeast (S. cerevisiae)"
      )
    ) +
    scale_y_continuous(limits = y_lim, breaks = seq(-3, 3, 1)) +
    labs(
      x     = "log10(peptide count)  [proxy de intensidad]",
      y     = "log2FC",
      title = title,
      color = NULL
    ) +
    theme_bw(base_size = 11) +
    theme(
      panel.grid.minor   = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_line(color = "grey90"),
      plot.title         = element_text(size = 11, face = "bold"),
      legend.position    = "bottom",
      legend.key.size    = unit(0.4, "cm")
    ) +
    guides(color = guide_legend(override.aes = list(size = 3, alpha = 1)))
}

# --- GENERAR FIGURA -------------------------------------------------------

panel_no_norm <- make_panel(
  data  = df, y_col = "LOG2(FOLD)",
  gt_h  = GT_HUMAN, gt_b = GT_BACTERIA, gt_y = GT_YEAST,
  title = "No Post-processing norm."
)

panel_median <- make_panel(
  data  = df, y_col = "log2FC_med",
  gt_h  = GT_HUMAN_med, gt_b = GT_BACTERIA_med, gt_y = GT_YEAST_med,
  title = "+median norm."
)

legend_shared <- get_legend(panel_no_norm)

panels <- plot_grid(
  panel_no_norm + theme(legend.position = "none"),
  panel_median  + theme(legend.position = "none"),
  ncol = 2, align = "hv"
)

final_fig <- plot_grid(panels, legend_shared, ncol = 1, rel_heights = c(1, 0.08))

ggsave(OUT_PNG, final_fig, width = 10, height = 5.5, dpi = 300)
ggsave(OUT_PDF, final_fig, width = 10, height = 5.5, device = cairo_pdf)
cat("Guardado:", OUT_PNG, "\n")
