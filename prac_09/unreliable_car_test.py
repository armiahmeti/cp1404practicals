"""Basic stochastic tests for UnreliableCar."""
import random
from unreliable_car import UnreliableCar


def main():
    random.seed(42)
    car = UnreliableCar("Dodgy", 1000, reliability=50)  # 50% reliable
    attempts = 200
    distance = 5
    results = [car.drive(distance) for _ in range(attempts)]
    drove_counts = sum(1 for d in results if d > 0)
    print(f"Drove on {drove_counts}/{attempts} attempts (~{drove_counts/attempts:.0%})")
    assert 50 - 20 <= (drove_counts / attempts) * 100 <= 50 + 20  # within +/-20%
    assert any(d == 0 for d in results) and any(d > 0 for d in results)
    print("UnreliableCar tests passed.")


if __name__ == "__main__":
    main()
