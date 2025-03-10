#!/usr/bin/env pwsh

$ROOT = Split-Path -Parent $PSSCRIPTROOT

$global:ProgressPreference  = 'SilentlyContinue'
$response = Invoke-WebRequest https://getbootstrap.com/
$downloadlink = $response.links | Where-Object { $_.href -like "*download/" } | foreach-object { $_.href } | select-object -first 1
$downloadpage = Invoke-WebRequest https://getbootstrap.com$downloadlink

$dist_download_url = $downloadpage.links | where-object { $_.href -like "*-dist.zip" } | foreach-object { $_.href }
$dist_version      = $dist_download_url.split("/")[-2].replace("v","")
$dist_zip          = "$ROOT\${dist_version}.zip"

Write-Host "Download $dist_zip from $dist_download_url"
Invoke-WebRequest $dist_download_url -O $dist_zip

Write-Host "Unpack to assets\vendor\bootstrap\${dist_version}"

$fldr_bootstrap = "project\dashboard\static\assets\vendor\bootstrap"

if (Test-Path -Path $fldr_bootstrap) {
    Remove-Item -recurse -force           $fldr_bootstrap
}

New-Item -type directory                  $fldr_bootstrap > $null
Expand-Archive $dist_zip -destinationpath $fldr_bootstrap

Move-Item $fldr_bootstrap\bootstrap* $fldr_bootstrap\${dist_version}

$global:ProgressPreference  = 'Continue'
