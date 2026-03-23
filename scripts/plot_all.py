import os
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BET_DIR = os.path.join(BASE_DIR, "BET")
TGA_DIR = os.path.join(BASE_DIR, "TGA")
TRANSPORT_DIR = os.path.join(BASE_DIR, "Transport")
OUTPUT_DIR = os.path.join(BASE_DIR, "figures")


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_bet_isotherm():
    file_path = os.path.join(BET_DIR, "isotherm_raw.csv")
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))
    plt.plot(df["Relative Pressure (P/P0)"], df["Adsorption_Untreated (cm3/g)"], marker="o", linewidth=1.8, label="Untreated - Adsorption")
    plt.plot(df["Relative Pressure (P/P0)"], df["Desorption_Untreated (cm3/g)"], marker="s", linewidth=1.5, linestyle="--", label="Untreated - Desorption")
    plt.plot(df["Relative Pressure (P/P0)"], df["Adsorption_Treated (cm3/g)"], marker="o", linewidth=1.8, label="Treated - Adsorption")
    plt.plot(df["Relative Pressure (P/P0)"], df["Desorption_Treated (cm3/g)"], marker="s", linewidth=1.5, linestyle="--", label="Treated - Desorption")

    plt.xlabel("Relative Pressure (P/P0)")
    plt.ylabel("Adsorbed Volume (cm³/g)")
    plt.title("BET Adsorption-Desorption Isotherms")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "bet_isotherm.png"), dpi=300)
    plt.close()


def plot_pore_distribution():
    file_path = os.path.join(BET_DIR, "pore_distribution.csv")
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))
    plt.plot(df["Pore Diameter (nm)"], df["Untreated_dV_dlogD (cm3/g)"], marker="o", linewidth=1.8, label="Untreated")
    plt.plot(df["Pore Diameter (nm)"], df["Treated_dV_dlogD (cm3/g)"], marker="o", linewidth=1.8, label="Treated")

    plt.xlabel("Pore Diameter (nm)")
    plt.ylabel("dV/dlogD (cm³/g)")
    plt.title("BJH Pore Size Distribution")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "pore_distribution.png"), dpi=300)
    plt.close()


def plot_tga():
    file_path = os.path.join(TGA_DIR, "tga_curve.csv")
    df = pd.read_csv(file_path)

    fig, ax1 = plt.subplots(figsize=(8, 6))

    ax1.plot(df["Temperature (C)"], df["Weight (%)"], marker="o", linewidth=1.8, label="TGA")
    ax1.set_xlabel("Temperature (°C)")
    ax1.set_ylabel("Weight (%)")

    ax2 = ax1.twinx()
    ax2.plot(df["Temperature (C)"], df["DTG_abs (wt_percent_per_C)"], marker="s", linewidth=1.5, linestyle="--", label="DTG")
    ax2.set_ylabel("DTG (wt.%/°C)")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

    plt.title("Thermogravimetric Analysis (TGA/DTG)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "tga_dtg.png"), dpi=300)
    plt.close()


def plot_transport():
    file_path = os.path.join(TRANSPORT_DIR, "diffusion_results.csv")
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 6))
    plt.bar(df["Sample"], df["Mean (m2/s)"], yerr=df["SD (m2/s)"], capsize=5)

    plt.xlabel("Sample")
    plt.ylabel("Diffusion Coefficient (m²/s)")
    plt.title("Transport Performance")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "transport_performance.png"), dpi=300)
    plt.close()


def main():
    ensure_output_dir()
    plot_bet_isotherm()
    plot_pore_distribution()
    plot_tga()
    plot_transport()
    print("All figures generated successfully in the 'figures' folder.")


if __name__ == "__main__":
    main()
