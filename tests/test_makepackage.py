def test_folders(testing_path):
    assert (testing_path / "venv-pkg").exists()

    assert (testing_path / "pkg").exists()
    assert (testing_path / "pkg" / "pkg").exists()
    assert (testing_path / "pkg" / "tests").exists()


def test_pkg_files_no_CLI(testing_path, files_no_CLI):
    root_dir = testing_path / "pkg"
    src_dir = root_dir / "pkg"
    tests_dir = root_dir / "tests"

    files = files_no_CLI

    assert all((root_dir / file).exists() for file in files["root"])
    assert all((src_dir / file).exists() for file in files["src"])
    assert all((tests_dir / file).exists() for file in files["test"])


def test_pkg_files_with_CLI(testing_path, files_with_CLI):
    root_dir = testing_path / "pkgCLI"
    src_dir = root_dir / "pkgCLI"
    tests_dir = root_dir / "tests"

    files = files_with_CLI

    assert all((root_dir / file).exists() for file in files["root"])
    assert all((src_dir / file).exists() for file in files["src"])
    assert all((tests_dir / file).exists() for file in files["test"])
