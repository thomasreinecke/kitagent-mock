# mock-agent/main.py
import time
import argparse
import json
import os

def train(config_path: str, output_path: str):
    """
    Simulates a training run.
    """
    print("--- Mock Agent Training Run Initializing ---")
    
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)
    print(f"Artifacts and logs will be saved to: {output_path}")

    # Load configuration
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        sleep_duration = config.get("sleep_duration", 10)
        print(f"Configuration loaded. Will simulate work for {sleep_duration} seconds.")
    except Exception as e:
        print(f"Error loading config from {config_path}: {e}")
        sleep_duration = 10

    # Simulate work
    for i in range(sleep_duration):
        print(f"Step {i+1}/{sleep_duration}: Processing data...")
        time.sleep(1)

    # Simulate creating an artifact in the specified output path
    try:
        artifact_file_path = os.path.join(output_path, "model.zip")
        with open(artifact_file_path, "w") as f:
            f.write("This is a dummy model artifact.")
        print(f"Dummy artifact created at: {artifact_file_path}")
    except Exception as e:
        print(f"Error creating dummy artifact: {e}")

    # Simulate writing metrics in the specified output path
    try:
        metrics_file_path = os.path.join(output_path, "metrics.log")
        with open(metrics_file_path, "w") as f:
            f.write("pnl,10.5\n")
            f.write("sharpe,0.8\n")
        print(f"Dummy metrics written to: {metrics_file_path}")
    except Exception as e:
        print(f"Error writing dummy metrics: {e}")

    print("--- Mock Agent Training Run Finished ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mock Agent for Kit Framework")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Train command ---
    train_parser = subparsers.add_parser("train", help="Simulate a training run")
    train_parser.add_argument("--config", required=True, help="Path to the configuration JSON file.")
    train_parser.add_argument("--output-path", required=True, help="Directory to save artifacts and logs.")

    # --- Test command (placeholder) ---
    test_parser = subparsers.add_parser("test", help="Simulate a testing run")

    args = parser.parse_args()

    if args.command == "train":
        train(args.config, args.output_path)
    elif args.command == "test":
        print("Mock test command executed.")