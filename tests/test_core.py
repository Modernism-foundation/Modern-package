from modern.core import ModernApp

def test_run(capsys):
    app = ModernApp()
    app.run()
    captured = capsys.readouterr()
    assert "Modern-package" in captured.out
