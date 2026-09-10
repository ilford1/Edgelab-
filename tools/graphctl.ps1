param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $GraphArguments
)

$ErrorActionPreference = 'Stop'
$graphScript = Join-Path $PSScriptRoot 'graphctl.py'
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$pyLauncher = Get-Command py -ErrorAction SilentlyContinue

if ($pythonCommand) {
    & $pythonCommand.Source $graphScript @GraphArguments
} elseif (Test-Path -LiteralPath $bundledPython) {
    & $bundledPython $graphScript @GraphArguments
} elseif ($pyLauncher) {
    & $pyLauncher.Source -3 $graphScript @GraphArguments
} else {
    throw 'Python 3 was not found on PATH and the Codex bundled runtime is unavailable.'
}

exit $LASTEXITCODE

