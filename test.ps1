param(
  [string]$Param1 = "test string"
)
$ErrorActionPreference = "Stop"

Write-Output "This is the string: $Param1."
