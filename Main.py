"""Creatore di grafici per risultati partite.

Questo script prende in input il numero di partite vinte, pareggiate e perse
e genera due grafici (bar + torta). Espone la funzione `create_charts`
per test non-interattivi e `main()` per l'uso da riga di comando.
"""
from typing import Optional
import matplotlib.pyplot as plt


def _validate_nonneg_int(value: str) -> int:
	try:
		n = int(value)
	except Exception:
		raise ValueError("Inserire un numero intero non negativo.")
	if n < 0:
		raise ValueError("Il valore non può essere negativo.")
	return n


def create_charts(wins: int, draws: int, losses: int, save_path: str = "grafico_partite.png", show: bool = True) -> str:
	"""Crea e salva due grafici (bar + pie) con i dati forniti.

	Args:
		wins: numero di partite vinte
		draws: numero di pareggi
		losses: numero di partite perse
		save_path: percorso file immagine di output
		show: se True apre la finestra grafica (utile in desktop)

	Returns:
		Il percorso del file salvato.
	"""
	labels = ["Vinte", "Pareggiate", "Perse"]
	values = [wins, draws, losses]

	fig, axes = plt.subplots(1, 2, figsize=(10, 4))

	# Bar chart
	ax_bar = axes[0]
	bars = ax_bar.bar(labels, values, color=["#4CAF50", "#FFD54F", "#F44336"])
	ax_bar.set_title("Risultati (conteggio)")
	ax_bar.set_ylabel("Partite")
	for bar in bars:
		height = bar.get_height()
		ax_bar.annotate(str(int(height)), xy=(bar.get_x() + bar.get_width() / 2, height),
						xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

	# Pie chart
	ax_pie = axes[1]
	total = sum(values)
	if total == 0:
		# per evitare divisione per zero, mostrare fette uguali ma indicare 0
		pie_values = [1, 1, 1]
		autopct = lambda pct: "0%"  # mostrare 0% quando totale 0
	else:
		pie_values = values
		autopct = "%1.1f%%"

	ax_pie.pie(pie_values, labels=labels, autopct=autopct, colors=["#4CAF50", "#FFD54F", "#F44336"], startangle=90)
	ax_pie.set_title("Distribuzione percentuale")

	fig.tight_layout()
	fig.savefig(save_path, dpi=150)
	if show:
		plt.show()
	else:
		plt.close(fig)
	return save_path


def main() -> None:
	print("Creatore di grafici — inserisci il numero di partite.")
	try:
		wins = _validate_nonneg_int(input("Numero di partite vinte: ").strip())
		draws = _validate_nonneg_int(input("Numero di partite pareggiate: ").strip())
		losses = _validate_nonneg_int(input("Numero di partite perse: ").strip())
	except ValueError as e:
		print(f"Input non valido: {e}")
		return
	except KeyboardInterrupt:
		print("\nInterrotto dall'utente.")
		return

	out = create_charts(wins, draws, losses, save_path="grafico_partite.png", show=True)
	print(f"Grafico creato e salvato in: {out}")


if __name__ == "__main__":
	main()