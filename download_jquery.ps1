#!/usr/bin/env pwsh

$ROOT = Split-Path -Parent $PSSCRIPTROOT

$version = "3.7.0"

$url_base = "https://code.jquery.com"

$destination = "project\dashboard\static\assets\vendor\jquery\$version\js"

Write-Host "Prepare  destination $destination"
if (Test-Path -Path $destination) {
    Remove-Item -recurse -force           $destination > $null
}

New-Item -type directory                  $destination > $null

Invoke-WebRequest $url_base/jquery-${version}.js      -O $destination/jquery-${version}.js
Invoke-WebRequest $url_base/jquery-${version}.min.map -O $destination/jquery-${version}.min.map
