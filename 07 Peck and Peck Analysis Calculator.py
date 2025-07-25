import tkinter as tk
from tkinter import ttk, messagebox

class PeckPeckAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Peck and Peck Analysis Calculator")
        self.root.geometry("900x700")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Result.TLabel', font=('Arial', 10, 'bold'), foreground='blue')
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', font=('Arial', 10))
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_input_tab()
        self.create_info_tab()
        
    def create_input_tab(self):
        # Input tab
        input_tab = ttk.Frame(self.notebook)
        self.notebook.add(input_tab, text="Analysis Calculator")
        
        # Header
        header_frame = ttk.Frame(input_tab)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="Peck and Peck Analysis", style='Header.TLabel').pack()
        ttk.Label(header_frame, text="Calculate crown dimension ratios for incisors").pack()
        
        # Input frame
        input_frame = ttk.LabelFrame(input_tab, text="Crown Diameter Measurements (in mm)", padding="15")
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Central Incisor measurements
        ttk.Label(input_frame, text="Central Incisor (11, 21)", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)
        
        # Mesiodistal width (ideal: 8.5 mm)
        ttk.Label(input_frame, text="Mesiodistal Crown Diameter:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.central_md = tk.DoubleVar(value=8.5)
        ttk.Entry(input_frame, textvariable=self.central_md, width=8).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Faciolingual width (ideal: 7.1 mm)
        ttk.Label(input_frame, text="Faciolingual Crown Diameter:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.central_fl = tk.DoubleVar(value=7.1)
        ttk.Entry(input_frame, textvariable=self.central_fl, width=8).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Lateral Incisor measurements
        ttk.Label(input_frame, text="\nLateral Incisor (12, 22)", font=('Arial', 10, 'bold')).grid(row=3, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)
        
        # Mesiodistal width (ideal: 6.5 mm)
        ttk.Label(input_frame, text="Mesiodistal Crown Diameter:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.lateral_md = tk.DoubleVar(value=6.5)
        ttk.Entry(input_frame, textvariable=self.lateral_md, width=8).grid(row=4, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Faciolingual width (ideal: 6.2 mm)
        ttk.Label(input_frame, text="Faciolingual Crown Diameter:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=2)
        self.lateral_fl = tk.DoubleVar(value=6.2)
        ttk.Entry(input_frame, textvariable=self.lateral_fl, width=8).grid(row=5, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(input_tab)
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(input_tab, text="Analysis Results", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Central incisor results
        ttk.Label(results_frame, text="Central Incisor Analysis:", font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        self.central_result = tk.Text(results_frame, height=4, wrap=tk.WORD, font=('Arial', 10))
        self.central_result.pack(fill=tk.X, pady=(0, 10))
        
        # Lateral incisor results
        ttk.Label(results_frame, text="Lateral Incisor Analysis:", font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        self.lateral_result = tk.Text(results_frame, height=4, wrap=tk.WORD, font=('Arial', 10))
        self.lateral_result.pack(fill=tk.X)
        
    def create_info_tab(self):
        # Information tab
        info_tab = ttk.Frame(self.notebook)
        self.notebook.add(info_tab, text="Information")
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(info_tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_scroll = ttk.Scrollbar(text_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        info_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=text_scroll.set, 
                          font=('Arial', 10), padx=10, pady=10)
        info_text.pack(fill=tk.BOTH, expand=True)
        
        text_scroll.config(command=info_text.yview)
        
        # Add information content
        info_content = """PECK AND PECK ANALYSIS INFORMATION

Measurement Instructions:
1. Measure on study casts or intraorally using a digital caliper
2. Mesiodistal diameter: Greatest distance between proximal surfaces at contact areas
3. Faciolingual diameter: Greatest distance between labial/buccal and lingual surfaces
4. Record measurements to the nearest 0.1 mm

Parameters:
- Peck and Peck Index = (Mesiodistal / Faciolingual) × 100
- Central Incisors: Teeth 11 and 21 (FDI numbering)
- Lateral Incisors: Teeth 12 and 22 (FDI numbering)

Ideal Values (based on Peck and Peck studies):
Central Incisors:
- Mesiodistal diameter: 8.5 mm (range 7.5-9.5 mm)
- Faciolingual diameter: 7.1 mm (range 6.5-7.7 mm)
- Ideal ratio: 88-92%

Lateral Incisors:
- Mesiodistal diameter: 6.5 mm (range 5.5-7.5 mm)
- Faciolingual diameter: 6.2 mm (range 5.5-6.9 mm)
- Ideal ratio: 90-95%

Interpretation Guidelines:
Central Incisors:
- Ratio > 92%: Mesiodistal width is excessive (consider interproximal reduction)
- Ratio < 88%: Normal or faciolingually dominant (no reduction needed)
- 88-92%: Proportional dimensions

Lateral Incisors:
- Ratio > 95%: Mesiodistal width is excessive (consider interproximal reduction)
- Ratio < 90%: Normal or faciolingually dominant (no reduction needed)
- 90-95%: Proportional dimensions

Clinical Significance:
- Helps identify teeth that may benefit from interproximal reduction (IPR)
- Useful for treatment planning in cases with:
  - Crowding
  - Bolton discrepancies
  - Tooth-size-arch-length discrepancies
- Particularly valuable for:
  - Peg-shaped laterals
  - Unusually shaped incisors
  - Cases requiring precise space management

Technique Notes:
1. Measure multiple teeth when possible
2. Consider tooth morphology and contact points
3. Combine with other diagnostic tools (Bolton analysis, space analysis)
4. Always verify clinically before performing IPR

Common Findings:
- High ratios often seen with:
  - Peg-shaped lateral incisors
  - Triangular-shaped teeth
  - Certain ethnic tooth morphologies
- Low ratios may indicate:
  - Lingually inclined teeth
  - Unusually thick teeth
  - Restorative modifications
"""
        info_text.insert(tk.END, info_content)
        info_text.config(state=tk.DISABLED)
    
    def calculate(self):
        try:
            # Calculate central incisor ratio
            central_md = self.central_md.get()
            central_fl = self.central_fl.get()
            
            if central_fl == 0:
                raise ValueError("Faciolingual diameter cannot be zero")
                
            central_ratio = (central_md / central_fl) * 100
            
            # Central incisor interpretation
            central_interpretation = f"Peck and Peck Index: {central_ratio:.1f}%\n"
            if central_ratio > 92:
                central_interpretation += "• Mesiodistal width is excessive (>92%)\n"
                central_interpretation += "• Consider interproximal reduction (IPR) if crowding exists\n"
                central_interpretation += "• Typical of triangular-shaped central incisors"
            elif central_ratio < 88:
                central_interpretation += "• Faciolingual width is dominant (<88%)\n"
                central_interpretation += "• IPR generally not recommended\n"
                central_interpretation += "• Common in thick or lingually inclined teeth"
            else:
                central_interpretation += "• Proportional dimensions (88-92%)\n"
                central_interpretation += "• Normal tooth morphology\n"
                central_interpretation += "• No IPR needed based on ratio alone"
            
            # Calculate lateral incisor ratio
            lateral_md = self.lateral_md.get()
            lateral_fl = self.lateral_fl.get()
            
            if lateral_fl == 0:
                raise ValueError("Faciolingual diameter cannot be zero")
                
            lateral_ratio = (lateral_md / lateral_fl) * 100
            
            # Lateral incisor interpretation
            lateral_interpretation = f"Peck and Peck Index: {lateral_ratio:.1f}%\n"
            if lateral_ratio > 95:
                lateral_interpretation += "• Mesiodistal width is excessive (>95%)\n"
                lateral_interpretation += "• Strong candidate for IPR if crowding exists\n"
                lateral_interpretation += "• Typical of peg-shaped lateral incisors"
            elif lateral_ratio < 90:
                lateral_interpretation += "• Faciolingual width is dominant (<90%)\n"
                lateral_interpretation += "• IPR generally contraindicated\n"
                lateral_interpretation += "• May indicate unusual tooth morphology"
            else:
                lateral_interpretation += "• Proportional dimensions (90-95%)\n"
                lateral_interpretation += "• Normal tooth morphology\n"
                lateral_interpretation += "• IPR decisions based on other factors"
            
            # Display results
            self.central_result.config(state=tk.NORMAL)
            self.central_result.delete(1.0, tk.END)
            self.central_result.insert(tk.END, central_interpretation)
            self.central_result.config(state=tk.DISABLED)
            
            self.lateral_result.config(state=tk.NORMAL)
            self.lateral_result.delete(1.0, tk.END)
            self.lateral_result.insert(tk.END, lateral_interpretation)
            self.lateral_result.config(state=tk.DISABLED)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except tk.TclError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def reset(self):
        # Reset to ideal values
        self.central_md.set(8.5)
        self.central_fl.set(7.1)
        self.lateral_md.set(6.5)
        self.lateral_fl.set(6.2)
        
        self.central_result.config(state=tk.NORMAL)
        self.central_result.delete(1.0, tk.END)
        self.central_result.config(state=tk.DISABLED)
        
        self.lateral_result.config(state=tk.NORMAL)
        self.lateral_result.delete(1.0, tk.END)
        self.lateral_result.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeckPeckAnalysisApp(root)
    root.mainloop()