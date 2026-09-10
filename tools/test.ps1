$ErrorActionPreference = 'Stop'
$workspaceRoot = Split-Path -Parent $PSScriptRoot
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$pyLauncher = Get-Command py -ErrorAction SilentlyContinue

if ($pythonCommand) {
    $interpreter = $pythonCommand.Source
    $prefix = @()
} elseif (Test-Path -LiteralPath $bundledPython) {
    $interpreter = $bundledPython
    $prefix = @()
} elseif ($pyLauncher) {
    $interpreter = $pyLauncher.Source
    $prefix = @('-3')
} else {
    throw 'Python 3 was not found on PATH and the Codex bundled runtime is unavailable.'
}

$env:PYTHONDONTWRITEBYTECODE = '1'
& $interpreter @prefix (Join-Path $PSScriptRoot 'graphctl.py') --root $workspaceRoot validate
if ($LASTEXITCODE -ne 0) { throw 'Graph validation failed.' }

Push-Location $workspaceRoot
try {
    & $interpreter @prefix -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { throw 'Test suite failed.' }
} finally {
    Pop-Location
}

