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
    hiddenimports=[],
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
