# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for SCLI — Security Posture Analysis Tool (Linux CLI)
# by Antibody Cyber Technology, LLC
#
# Build:  pyinstaller SCLI.spec
# Output: dist/SCLI  (single self-contained binary)

a = Analysis(
    ['SCLI'],
    pathex=[],
    binaries=[],
    datas=[
        ('spat_cli/spat_cli.py', 'spat_cli'),
    ],
    # spat_cli.py is bundled as a data file so PyInstaller never analyses its
    # imports.  List them explicitly so they are included in the binary.
    hiddenimports=[
        'json', 'socket', 'ssl', '_ssl', 'struct', 'time', 'threading',
        'warnings', 'collections', 'base64', 'argparse',
        'concurrent', 'concurrent.futures',
        'datetime', 'pathlib',
        'urllib', 'urllib.parse', 'urllib.request', 'urllib.error',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SCLI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,          # CLI tool — keep console visible
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
