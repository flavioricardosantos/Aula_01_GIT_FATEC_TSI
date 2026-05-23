import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class JanelaSenoSeaborn(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numpy + Seaborn no PyQt5")
        self.setGeometry(100, 100, 800, 600)

        # 1. Configuração do visual do Seaborn (isso afeta todos os gráficos)
        sns.set_theme(style="darkgrid") # Pode ser "whitegrid", "dark", "ticks"

        # 2. Setup da Interface
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        # 3. Criar a figura do Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        self.figure, self.ay = plt.subplots(figsize=(5, 4))
        self.new_canva = FigureCanvas(self.figure)
        layout.addWidget(self.new_canva)


        self.homens = QLabel('blablabal')
        layout.addWidget(self.homens)


        self.desenhar_com_numpy()
        self.pizza()

    def desenhar_com_numpy(self):
        meses_x = list(range(12))
        valores_y = [10, 25, 15, 30, 20, 25, 30, 40, 45, 20, 10, 15]
        meses = ['jan.', 'fev.', 'mar.', 'abr.', 'mai.', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']

        # Usando o Seaborn para plotar os arrays do Numpy
        # lineplot é o equivalente "bonito" do plt.plot
        sns.lineplot(x=meses_x, y=valores_y, ax=self.ax, marker='o', color="coral", linewidth=2.5)

        # Customização adicional
        self.ax.set_xticks(meses_x)
        self.ax.set_xticklabels(meses)

        self.ax.set_title("Onda Senoidal com Estilo Seaborn")
        self.ax.set_xlabel("Tempo (s)")
        self.ax.set_ylabel("Amplitude")

        self.canvas.draw()
    
    def pizza(self):
        genero = ['feminino', 'masculino']
        valores = [150, 80]

        centro = plt.Circle((0,0), 0.70, fc = 'white')
        cores = sns.color_palette('pastel')[0:2]
        self.ay.clear()

        self.ay.pie(
            valores,
            colors=cores,
            autopct='%1.1f%%',
            startangle=140,
            shadow=False
        )

        self.homens.setText(float((150/(150 + 80)) * 100))

        self.ay.add_artist(centro)
        self.ay.set_title('Distribuição por gênero')
        self.ay.axis('equal')
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaSenoSeaborn()
    janela.show()
    sys.exit(app.exec_())