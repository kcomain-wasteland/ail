with import <nixpkgs> {}; mkShellNoCC {
    packages = [
        (python3Packages.transformers.overrideAttrs (final: {
            dependencies = final.dependencies ++ [
                python3Packages.bitsandbytes
            ];
        }))
        python3Packages.pytorch
        python3Packages.requests
        python3Packages.accelerate
        python3Packages.bitsandbytes
        (python3Packages.buildPythonPackage rec {
            pname = "quanto";
            version = "0.2.0";
            src = python3Packages.fetchPypi {
                inherit pname version;
                hash = "sha256-HVWdudXQ86RUj6EaB9WrqHXD3cl+xoWRrZrsXMAj4Qw=";
            };
            pyproject = true;
            build-system = with python3Packages; [
                setuptools
                setuptools-scm
            ];

            dependencies = with python3Packages; [
                pytorch
                ninja
                numpy
                safetensors
            ];
        })
    ];
}
