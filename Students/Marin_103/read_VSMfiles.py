import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import filedialog
import time

plt.style.use('ggplot')

# Function to get the file path from the user
def get_file_path():
  """
  Opens a file dialog and returns the chosen file path.
  """
  return filedialog.askopenfilename()

# Main script
file_path = get_file_path()  # Get file path from user

try:
    # Assuming data is in a structured format like CSV or similar
    df = pd.read_csv(file_path, delimiter=',', encoding='Latin-1', skiprows=30)
    # Process the DataFrame
 
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
## Leer el valor de masa ####
df_m = pd.read_csv(file_path, delimiter='\t', encoding='Latin-1', nrows=21).iloc[19]
split_data = df_m.str.split(",", expand=True)
masa = float(split_data.iloc[0, 1])*1E-3
######

df_dropped = df[['Temperature (K)', 'Magnetic Field (Oe)', 'Moment (emu)']]
df_dropped['M (emu/g)'] = df_dropped['Moment (emu)']/masa


df_dropped.plot(x='Magnetic Field (Oe)', y='M (emu/g)', kind='scatter', color = 'red')

plt.title('M vs H')
plt.ticklabel_format(useOffset=False, style='plain')
plt.grid(True)
plt.show()


df_dropped.plot(x='Temperature (K)', y='M (emu/g)', kind='scatter', color = 'green')
plt.grid(True)
plt.ticklabel_format(useOffset=False, style='plain')
plt.title('M vs T')
plt.show()


df_dropped = df_dropped.dropna(how='any')
df_dropped['Masa (g)'] = masa
## Guardar el archivo ##

new_path = file_path.replace(".DAT", ".csv") 
df_dropped.to_csv(new_path, index=False, decimal = ',')  # Optional: exclude index

print(f"Data saved successfully to: {new_path}")
time.sleep(5)