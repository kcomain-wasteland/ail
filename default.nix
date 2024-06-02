with import <nixpkgs> {}; mkShellNoCC {
    packages = [
        python3Packages.requests
        python3Packages.cohere
        python3Packages.python-dotenv
    ];
}
