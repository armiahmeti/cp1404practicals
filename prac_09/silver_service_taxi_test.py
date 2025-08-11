"""Tests for SilverServiceTaxi fares and string formatting."""
from silver_service_taxi import SilverServiceTaxi


def main():
    limo = SilverServiceTaxi("Limo", 100, fanciness=2)
    limo.start_fare()
    limo.drive(18)
    fare = limo.get_fare()
    print(limo)
    print(f"Fare for 18 km (fanciness=2): ${fare:.2f}")
    assert abs(fare - 48.80) < 0.001  # expects rounding to nearest 10c in Taxi then + 4.50 flagfall
    print("SilverServiceTaxi tests passed.")


if __name__ == "__main__":
    main()
