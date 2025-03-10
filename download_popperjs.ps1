#!/usr/bin/env pwsh

$ROOT = Split-Path -Parent $PSSCRIPTROOT

$version = "2.11.8"

$url_base = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/${version}/umd/"

$destination = "project\dashboard\static\assets\vendor\popperjs\$version\js"

Write-Host "Prepare  destination $destination"
if (Test-Path -Path $destination) {
    Remove-Item -recurse -force           $destination > $null
}

New-Item -type directory                  $destination > $null

Invoke-WebRequest $url_base/popper.js -O  $destination/popper.js
