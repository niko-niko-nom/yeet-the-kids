{
  description = "Yeet the kids";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system: 
    let
      pkgs = (import nixpkgs) { inherit system; };
    in {
      devShell = pkgs.mkShell {
        name = "Yeet the Kids";
        buildInputs = with pkgs; [
          python312
          python312Packages.django
          python312Packages.pillow
        ];

        shellHook = ''
          echo ""
          python --version
          echo "
          Welcome to the Yeet the Kids shell 🚀!
          ";
        '';
      };
    }
  );
}
