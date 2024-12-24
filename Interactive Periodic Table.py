import Data
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Interactive Periodic Table")
root.state('zoomed')
paned_window = tk.PanedWindow(root, orient="horizontal")
paned_window.pack(fill="both", expand=True)
main_window = tk.PanedWindow(paned_window, orient='vertical', width=1135)
paned_window.add(main_window)
sub_window = tk.PanedWindow(paned_window, orient='vertical')
paned_window.add(sub_window)
frame00 = tk.Frame(sub_window)
frame0 = tk.Frame(sub_window)
frame1 = tk.Frame(main_window, height=1000)
frame2 = tk.Frame(main_window)
sub_window.add(frame00)
sub_window.add(frame0)
main_window.add(frame1)
main_window.add(frame2)

canvas = tk.Canvas(frame0,height=100)
canvas.pack(side="left", fill="both", expand=True)
scrollbar = tk.Scrollbar(frame0, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def update_scroll_region(event=None):
    canvas.config(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", update_scroll_region)

tooltip = tk.Label(root, text="", bg="white", padx=10, pady=5, wraplength=200)

positions = {}
i = 1
j = 1
for key in Data.elements.keys():
    if (Data.elements[key]["Period"] == 6 and Data.elements[key]["Group"] == 3):
        positions[key] = (Data.elements[key]["Period"] + 3, Data.elements[key]["Group"] + i)
        i += 1
    elif (Data.elements[key]["Period"] == 7 and Data.elements[key]["Group"] == 3):
        positions[key] = (Data.elements[key]["Period"] + 3, Data.elements[key]["Group"] + j)
        j += 1
    else:
        positions[key] = (Data.elements[key]["Period"], Data.elements[key]["Group"])

checkbox_labels = [
    'Name', 'Atomic Number', 'Atomic Mass', 'Ionization Energy', 'Electron Configuration', 'Electronegativity',
    'Electron Affinity', 'Thermal Conductivity', 'Electrical Conductivity', 'Atomic Radius', 'Ionic Radius',
    'Covalent Radius', 'Atomic Volume', 'Density', 'Crystal Structure', 'Heat of Fusion', 'Heat of Vaporization',
    'Specific Heat Capacity', 'Oxidation States', 'Magnetic Properties', 'Refractive Index', 'Reactivity',
    'Electrochemical Potential', 'Flammability', 'Isotopes', 'Half Life', 'Radioactivity', 'Nuclear Binding Energy',
    'Decay Modes', 'Toxicity', 'Abundance', 'Hardness', 'Color', 'Melting Point', 'Boiling Point', 'State at Standard Conditions'
]
checkbox_vars=[]
for label in checkbox_labels:
    if label=='Name' or label=='Atomic Number' or label=='Atomic Mass':
        checkbox_vars.append(tk.BooleanVar(value=True))
    else:
        checkbox_vars.append(tk.BooleanVar(value=False))
for idx, (var, label) in enumerate(zip(checkbox_vars, checkbox_labels)):
    row = idx // 1
    column = idx % 1
    checkbox = tk.Checkbutton(scrollable_frame, text=label, variable=var)
    checkbox.grid(row=row, column=column, padx=5, pady=5, sticky="nw")

def update_requested_keys():
    requested_keys = []
    for var, key in zip(checkbox_vars, checkbox_labels):
        if var.get():
            requested_keys.append(key)
    return requested_keys

def datails(symbol,type):
    element = Data.elements[symbol]
    details = {
    'Name': element['Name'],
    'Atomic Number': element['Atomic Number'],
    'Atomic Mass': element['Atomic Mass'],
    'Ionization Energy': element['Ionization Energy'],
    'Electron Configuration': element['Electron Configuration'],
    'Electronegativity': element['Electronegativity'],
    'Electron Affinity': element['Electron Affinity'],
    'Thermal Conductivity': element['Thermal Conductivity'],
    'Electrical Conductivity': element['Electrical Conductivity'],
    'Atomic Radius': element['Atomic Radius'],
    'Ionic Radius': element['Ionic Radius'],
    'Covalent Radius': element['Covalent Radius'],
    'Atomic Volume': element['Atomic Volume'],
    'Density': element['Density'],
    'Crystal Structure': element['Crystal Structure'],
    'Heat of Fusion': element['Heat of Fusion'],
    'Heat of Vaporization': element['Heat of Vaporization'],
    'Specific Heat Capacity': element['Specific Heat Capacity'],
    'Oxidation States': element['Oxidation States'],
    'Magnetic Properties': element['Magnetic Properties'],
    'Refractive Index': element['Refractive Index'],
    'Reactivity': element['Reactivity'],
    'Electrochemical Potential': element['Electrochemical Potential'],
    'Flammability': element['Flammability'],
    'Isotopes': element['Isotopes'],
    'Half Life': element['Half Life'],
    'Radioactivity': element['Radioactivity'],
    'Nuclear Binding Energy': element['Nuclear Binding Energy'],
    'Decay Modes': element['Decay Modes'],
    'Toxicity': element['Toxicity'],
    'Abundance': element['Abundance'],
    'Hardness': element['Hardness'],
    'Color': element['Color'],
    'Melting Point': element['Melting Point'],
    'Boiling Point': element['Boiling Point'],
    'State at Standard Conditions': element['State at Standard Conditions']
}
    filtered_details={}
    if type=='pop':
        return details
    elif type=='tool':
        requested_keys=update_requested_keys()
        filtered_details = {key: details[key] for key in requested_keys}
        filtered_text = "\n".join([f"{key}: {value}" for key, value in filtered_details.items()])
        return filtered_text

def show_detail(event, symbol):
    tooltip.config(text=datails(symbol,'tool'))
    tooltip.place(x=event.x_root - root.winfo_x(), y=event.y_root - root.winfo_y())

def hide_detail(event):
    tooltip.place_forget()

def show_popup(symbol):
    popup = tk.Toplevel()
    popup.title(f"Details of {symbol}")
    popup_width = 650
    popup_height = 400
    main_width = root.winfo_width()
    main_height = root.winfo_height()
    main_x = root.winfo_x()
    main_y = root.winfo_y()
    center_x = main_x + (main_width - popup_width) // 2
    center_y = main_y + (main_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{center_x}+{center_y}")
    table = ttk.Treeview(popup, columns=("Property", "Value"), show="headings")
    table.heading("Property", text="Property")
    table.heading("Value", text="Value")
    table.column("Property", width=150)
    table.column("Value", width=400)
    details=datails(symbol,'pop')
    for property, value in details.items():
        table.insert("", "end", values=(property, value))
    table.pack(fill="both", expand=True, padx=10, pady=10)

category_color = {
    "Non-metal": "red",
    "Alkaline Earth Metal":"#ffcc80",
    "Alkali Metal":"#ffe0b2",
    "Noble Gas": "lightblue",
    "Metalloid":"steelblue",
    "Halogen":"#a6d7a6",
    "Post-transition Metal":"lightgray",
    "Transition Metal":"#d3c7e8",
    "Lanthanide":"#ffcdd3",
    "Actinide":"#ffab91"
    }

superscript_map = {
    '0': '\u2070', '1': '\u00B9', '2': '\u00B2', '3': '\u00B3',
    '4': '\u2074', '5': '\u2075', '6': '\u2076', '7': '\u2077',
    '8': '\u2078', '9': '\u2079'}

def convert_to_superscript(text):
    return ''.join(superscript_map.get(char, char) for char in text)

for symbol, pos in positions.items():
    color = category_color.get(Data.elements[symbol]["Category"])
    button = tk.Button(frame1, text=f"{symbol}{convert_to_superscript(str(Data.elements[symbol]["Atomic Number"]))}",\
    bg=color, width=5, height=2, command=lambda s=symbol: show_popup(s))
    button.grid(row=pos[0], column=pos[1], padx=5, pady=5)
    button.bind("<Enter>", lambda event, s=symbol: show_detail(event, s))
    button.bind("<Leave>", hide_detail)

def on_click(event):
    current_text = search_entry.get()
    if current_text == "Search":
        search_entry.delete(0, tk.END)

def on_focusout(event):
    search_entry.delete(0, tk.END)
    search_entry.insert(0, "Search")

def show_search_results(matching_results):
    popup = tk.Toplevel(frame00)
    popup.title("Search Results")
    popup.geometry("400x200")
    canvas = tk.Canvas(popup, height=100)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(popup, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollable_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    def update_scroll_region(event=None):
        canvas.config(scrollregion=canvas.bbox("all"))
    scrollable_frame.bind("<Configure>", update_scroll_region)
    i = 0
    for i in range(30):
        empty_label00 = tk.Label(scrollable_frame)
        empty_label00.grid(row=1, column=i, sticky="w")
    for symbol in matching_results:
        result_label = tk.Label(scrollable_frame, text=symbol, fg="blue", cursor="hand2")
        result_label.grid(row=i, column=30, sticky="w", padx=5, pady=2)
        result_label.bind("<Button-1>", lambda event, s=symbol, p=popup: on_label_click(s, p))
        i += 1

def on_label_click(symbol, popup):
    show_popup(symbol)
    popup.destroy()

def search_action(event=None):
    query = search_entry.get()
    if query:
        if query.isalpha():
            matching_results=[]
            for symbol in Data.elements:
                if query in Data.elements[symbol]["Name"].lower() or query in symbol.lower():
                    matching_results += [symbol]
            list(set(matching_results))
        elif query.isdigit():
            for symbol in Data.elements:
                if int(query)==int(Data.elements[symbol]["Atomic Number"]):
                    matching_results=[symbol]
            search_label.focus_set()
        if matching_results:
            if len(matching_results)>1:
                show_search_results(matching_results)
            else:
                show_popup(matching_results[0])
    search_label.focus_set()

search_label = tk.Label(frame00)
search_label.pack(padx=10, pady=1)
search_entry = tk.Entry(frame00, width=50)
search_entry.insert(0, "Search")
search_entry.pack(side="left", padx=10)
search_entry.bind("<FocusIn>", on_click)
search_entry.bind("<FocusOut>", on_focusout)
search_button = tk.Button(frame00, text="Search", command=search_action)
search_button.pack(side="left")

for group in range(1,19):
    group_label = tk.Label(frame1, text=group, width=5, height=2)
    group_label.grid(row=0, column=group, padx=5, pady=5)
for period in range(1,8):
    period_label = tk.Label(frame1, text=period, width=5, height=2)
    period_label.grid(row=period, column=0, padx=5, pady=5)
empty_label = tk.Label(frame1, text="", width=5, height=2)
empty_label.grid(row=0, column=0, padx=5, pady=5)
empty_label1 = tk.Label(frame1, text="", width=5, height=2)
empty_label1.grid(row=8, column=0, padx=5, pady=5)
empty_label2 = tk.Label(frame1, text="", width=1, height=1)
empty_label2.grid(row=10, column=0, padx=1, pady=1)
lanthanide = tk.Label(frame1, text="57-71", width=5, height=2, bg="#ffcdd3")
lanthanide.grid(row=6, column=3, padx=5, pady=5)
Actinide = tk.Label(frame1, text="89-103", width=5, height=2, bg="#ffab91")
Actinide.grid(row=7, column=3, padx=5, pady=5)
for a in range(2):
    empty_label3 = tk.Label(frame2, text="", width=5, height=2)
    empty_label3.grid(row=a, column=0, padx=5, pady=5)

c=0
r=0
for key in category_color.keys():
    label1=tk.Label(frame2, text="", width=1, height=1, bg=category_color[key])
    label1.grid(row=r,column=1+c,padx=1,pady=1)
    c+=1
    label2=tk.Label(frame2, text=key, height=1)
    label2.grid(row=r,column=1+c,padx=1,pady=1)
    c+=1
    if c==10:
        c=0
        r+=1

tooltip.lift()
root.mainloop()