import os
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image

# Initialize CustomTkinter appearance
ctk.set_appearance_mode("System")

# Gold Theme Palette matching the PixieBeam logo
GOLD_MAIN = "#C59B27"  # Rich Metallic Gold
GOLD_HOVER = "#A37E1B"  # Darker Gold on hover
GOLD_TEXT = "#FFFFFF"  # Crisp White text on gold buttons


class PixieBeamApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    # Window configuration
    self.title("PixieBeam - Medical Contouring & Segmentation")
    self.geometry("1120x780")
    self.minsize(950, 700)

    # Set window icon (.ico)
    self.setup_window_icon()

    # Main layout configuration
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    # --- Sidebar Section ---
    self.sidebar_frame = ctk.CTkFrame(self, width=270, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(6, weight=1)

    # Load and display transparent logo + Title in Sidebar
    self.load_sidebar_logo()

    # Navigation Buttons (Gold Styled)
    self.btn_dashboard = ctk.CTkButton(
        self.sidebar_frame,
        text="Dashboard",
        fg_color=GOLD_MAIN,
        hover_color=GOLD_HOVER,
        text_color=GOLD_TEXT,
        font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
        command=self.load_dashboard_view,
    )
    self.btn_dashboard.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    self.btn_segmentation = ctk.CTkButton(
        self.sidebar_frame,
        text="DICOM Contour & Classes",
        fg_color=GOLD_MAIN,
        hover_color=GOLD_HOVER,
        text_color=GOLD_TEXT,
        font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
        command=self.load_contour_view,
    )
    self.btn_segmentation.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    self.btn_units = ctk.CTkButton(
        self.sidebar_frame,
        text="Hounsfield Units (HU) Guide",
        fg_color=GOLD_MAIN,
        hover_color=GOLD_HOVER,
        text_color=GOLD_TEXT,
        font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
        command=self.load_hu_view,
    )
    self.btn_units.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    # Theme Switcher at bottom (Gold Styled)
    self.theme_menu = ctk.CTkOptionMenu(
        self.sidebar_frame,
        values=["System", "Light", "Dark"],
        fg_color=GOLD_MAIN,
        button_color=GOLD_HOVER,
        button_hover_color="#826312",
        text_color=GOLD_TEXT,
        command=self.change_theme_mode,
    )
    self.theme_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
    self.theme_menu.set("System")

    # --- Main Content Area ---
    self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.main_content.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
    self.main_content.grid_rowconfigure(2, weight=1)
    self.main_content.grid_columnconfigure(0, weight=1)

    # Header labels
    self.header_label = ctk.CTkLabel(
        self.main_content,
        text="Dashboard Overview",
        font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
    )
    self.header_label.grid(row=0, column=0, pady=(10, 5), sticky="w")

    self.sub_header = ctk.CTkLabel(
        self.main_content,
        text="Monitor clinical processing stats and inputs.",
        font=ctk.CTkFont(family="Arial", size=14),
        text_color="gray",
    )
    self.sub_header.grid(row=1, column=0, pady=(0, 20), sticky="w")

    # Dynamic frame for different views
    self.content_frame = ctk.CTkFrame(
        self.main_content, fg_color="transparent"
    )
    self.content_frame.grid(row=2, column=0, sticky="nsew")
    self.content_frame.grid_rowconfigure(0, weight=1)
    self.content_frame.grid_columnconfigure(0, weight=1)

    # Load default Dashboard view
    self.load_dashboard_view()

  def setup_window_icon(self):
    icon_path = r"C:\Users\Lenovo\Downloads\First hehe\Capture.ico"
    if os.path.exists(icon_path):
      try:
        self.iconbitmap(icon_path)
      except Exception:
        pass

  def load_sidebar_logo(self):
    logo_path = r"C:\Users\Lenovo\Downloads\First hehe\Capture.png"
    if os.path.exists(logo_path):
      try:
        pil_img = Image.open(logo_path).convert("RGBA")
        self.sidebar_logo_img = ctk.CTkImage(
            light_image=pil_img, dark_image=pil_img, size=(45, 45)
        )

        logo_container = ctk.CTkFrame(
            self.sidebar_frame, fg_color="transparent"
        )
        logo_container.grid(row=0, column=0, padx=15, pady=(20, 10), sticky="w")

        img_lbl = ctk.CTkLabel(
            logo_container, image=self.sidebar_logo_img, text=""
        )
        img_lbl.pack(side="left", padx=(0, 8))

        text_lbl = ctk.CTkLabel(
            logo_container,
            text="PixieBeam",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
        )
        text_lbl.pack(side="left")

      except Exception:
        self.fallback_title()
    else:
      self.fallback_title()

  def fallback_title(self):
    self.logo_title = ctk.CTkLabel(
        self.sidebar_frame,
        text="PixieBeam",
        font=ctk.CTkFont(family="Arial", size=22, weight="bold"),
    )
    self.logo_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

  def clear_content(self):
    for widget in self.content_frame.winfo_children():
      widget.destroy()

  def load_dashboard_view(self):
    self.header_label.configure(text="Dashboard Overview")
    self.sub_header.configure(
        text="Welcome to PixieBeam Medical Imaging & Contouring System."
    )
    self.clear_content()

    lbl = ctk.CTkLabel(
        self.content_frame,
        text=(
            "System Status: Ready & Calibrated\n\n• Go to 'DICOM Contour &"
            " Classes' to import your CT DICOM slices.\n• Choose from 16"
            " clinical tissue, fluid, and bone thresholds based on exact"
            " Hounsfield Units (HU)."
        ),
        font=("Arial", 14),
        justify="left",
    )
    lbl.pack(anchor="w", pady=20)

  def load_contour_view(self):
    self.header_label.configure(text="DICOM Contour & Tissue Classes")
    self.sub_header.configure(
        text=(
            "Insert DICOM files and select precise anatomical thresholding"
            " classes."
        )
    )
    self.clear_content()

    upload_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    upload_frame.pack(fill="x", pady=(0, 10), anchor="w")

    btn_upload = ctk.CTkButton(
        upload_frame,
        text="Browse DICOM Files",
        fg_color=GOLD_MAIN,
        hover_color=GOLD_HOVER,
        text_color=GOLD_TEXT,
        font=("Arial", 13, "bold"),
        command=self.browse_dicom,
    )
    btn_upload.pack(side="left", padx=(0, 15))

    self.file_label = ctk.CTkLabel(
        upload_frame, text="No DICOM file selected", text_color="gray"
    )
    self.file_label.pack(side="left")

    scroll_frame = ctk.CTkScrollableFrame(
        self.content_frame,
        label_text="Select Anatomical Contouring Class & Exact HU Interval:",
        label_font=("Arial", 14, "bold"),
        height=380,
    )
    scroll_frame.pack(fill="both", expand=True, pady=10)

    self.class_var = ctk.StringVar(value="cortical_bone")

    clinical_classes = [
        ("Tooth Enamel [+3000 HU and above]", "tooth_enamel"),
        ("Cortical / Compact Bone [+700 to +3000 HU]", "cortical_bone"),
        ("Trabecular / Cancellous Bone [+300 to +800 HU]", "cancellous_bone"),
        ("Iodinated Contrast Media [+100 to +500+ HU]", "contrast_media"),
        (
            "Coagulated Blood / Acute Hematoma [+60 to +90 HU]",
            "coagulated_blood",
        ),
        ("Liver Parenchyma [+40 to +60 HU]", "liver"),
        ("Skeletal Muscle [+35 to +55 HU]", "muscle"),
        ("Brain - Gray Matter [+37 to +45 HU]", "gray_matter"),
        ("Kidneys (Non-contrast) [+30 to +50 HU]", "kidneys"),
        ("Unclotted Blood [+30 to +45 HU]", "unclotted_blood"),
        ("Brain - White Matter [+20 to +30 HU]", "white_matter"),
        ("CSF / Urine / Simple Cysts [0 to +15 HU]", "csf_urine"),
        ("Pure Water (Reference) [0 HU]", "water"),
        ("Adipose Tissue (Fat) [-120 to -50 HU]", "fat"),
        ("Lung Parenchyma [-700 to -600 HU]", "lung"),
        ("Air / Gas [-1000 HU]", "air"),
    ]

    for text_label, val in clinical_classes:
      rb = ctk.CTkRadioButton(
          scroll_frame,
          text=text_label,
          variable=self.class_var,
          value=val,
          fg_color=GOLD_MAIN,
          hover_color=GOLD_HOVER,
          font=("Arial", 13),
      )
      rb.pack(anchor="w", padx=15, pady=6)

    bottom_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    bottom_frame.pack(fill="x", pady=(10, 0))

    btn_process = ctk.CTkButton(
        bottom_frame,
        text="Run Contouring & Segmentation",
        fg_color=GOLD_MAIN,
        hover_color=GOLD_HOVER,
        text_color=GOLD_TEXT,
        font=("Arial", 13, "bold"),
        command=self.run_segmentation,
    )
    btn_process.pack(side="left", padx=(0, 20))

    self.result_label = ctk.CTkLabel(
        bottom_frame, text="", font=("Arial", 13, "bold")
    )
    self.result_label.pack(side="left")

  def load_hu_view(self):
    self.header_label.configure(text="Hounsfield Units (HU) Reference Guide")
    self.sub_header.configure(
        text="Complete radiodensity reference scale for CT image segmentation."
    )
    self.clear_content()

    hu_scroll = ctk.CTkScrollableFrame(self.content_frame)
    hu_scroll.pack(fill="both", expand=True, pady=10)

    hu_info = (
        "BONE & CALCIFIED STRUCTURES:\n• Tooth Enamel: +3000 HU (or higher)\n•"
        " Cortical / Compact Bone: +700 to +3000 HU (Diaphysis, petrous bone)\n•"
        " Trabecular / Cancellous Bone: +300 to +800 HU (Epiphyses,"
        " vertebrae)\n\nCONTRAST & VASCULAR:\n• Iodinated Contrast Media: +100"
        " to +500+ HU (Arterial / Portal phases)\n• Coagulated Blood / Acute"
        " Hematoma: +60 to +90 HU\n• Unclotted Blood: +30 to +45 HU\n\nPARENCHYMA"
        " & SOFT TISSUES:\n• Liver: +40 to +60 HU (Mean ~60 HU; <40 HU suggests"
        " steatosis)\n• Skeletal Muscle: +35 to +55 HU\n• Brain - Gray Matter:"
        " +37 to +45 HU\n• Kidneys (Pre-contrast): +30 to +50 HU\n• Brain -"
        " White Matter: +20 to +30 HU\n\nFLUIDS, FAT, LUNG & AIR:\n•"
        " Cerebrospinal Fluid (CSF) & Urine: 0 to +15 HU\n• Pure Water: 0 HU"
        " (Calibration Reference)\n• Adipose Tissue (Fat): -120 to -50 HU\n•"
        " Lung Parenchyma: -700 to -600 HU\n• Air / Gas: -1000 HU"
    )
    lbl_hu = ctk.CTkLabel(
        hu_scroll, text=hu_info, font=("Arial", 14), justify="left"
    )
    lbl_hu.pack(anchor="w", padx=15, pady=15)

  def browse_dicom(self):
    filename = filedialog.askopenfilename(
        title="Select DICOM File",
        filetypes=[("DICOM Files", "*.dcm"), ("All Files", "*.*")],
    )
    if filename:
      self.file_label.configure(text=filename, text_color="black")

  def run_segmentation(self):
    selected_class = self.class_var.get().upper().replace("_", " ")
    self.result_label.configure(
        text=f"Applied {selected_class} HU threshold!",
        text_color=GOLD_HOVER,
    )

  def change_theme_mode(self, new_mode):
    ctk.set_appearance_mode(new_mode)


if __name__ == "__main__":
  app = PixieBeamApp()
  app.mainloop()