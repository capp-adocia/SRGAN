from collections import OrderedDict

import torch

import argparse


def main(args):
    # Process parameter dictionary
    state_dict = torch.load(args.inputs_model_path, map_location=torch.device("cpu"))["state_dict"]
    new_state_dict = OrderedDict()

    # Delete _orig_mod. in the parameter name
    for k, v in state_dict.items():
        name = k[10:]
        new_state_dict[name] = v

    torch.save({"state_dict": new_state_dict}, args.output_model_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs_model_path", type=str, help="Path to the model to be converted")
    parser.add_argument("--output_model_path", type=str, help="Path to the converted model")
    args = parser.parse_args()
    main(args)
