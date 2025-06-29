# PowerShell script to convert Pokemon Amber story markdown files to XML format
# Creates a new directory with XML chapters and _meta.xml




# powershell -ExecutionPolicy Bypass -File scripts/convert_to_xml.ps1

function Extract-ChapterNumber {
    param([string]$filename)
    if ($filename -match 'chapter(\d+)') {
        return [int]$matches[1]
    }
    return 0
}

function Escape-XML {
    param([string]$text)
    return $text -replace '&', '&amp;' -replace '<', '&lt;' -replace '>', '&gt;' -replace '"', '&quot;' -replace "'", '&apos;'
}

function Extract-TitleAndContent {
    param([string]$filePath)
    
    $content = Get-Content -Path $filePath -Raw -Encoding UTF8
    $lines = $content -split "`n"
    
    if ($lines[0] -match '^# (.+)$') {
        $title = $matches[1].Trim()
        $contentBody = ($lines[1..($lines.Length-1)] -join "`n").Trim()
        return @{
            Title = $title
            Content = $contentBody
        }
    } else {
        return @{
            Title = "Chapter $(Split-Path -Leaf $filePath)"
            Content = $content
        }
    }
}

function Create-XMLChapter {
    param([string]$title, [string]$content)
    
    $titleEscaped = Escape-XML $title
    $contentEscaped = Escape-XML $content
    
    return "<Chapter title=`"$titleEscaped`">`n$contentEscaped`n</Chapter>"
}

function Create-MetadataXML {
    param([array]$chaptersInfo)
    
    $currentDate = Get-Date -Format "yyyy-MM-dd"
    
    $metadataXML = @"
<StoryMetadata>
    <Title>Pokemon: Ambertwo</Title>
    <Author>ChronicImmortality</Author>
    <Synopsis>
    Pokemon fan gets isekai'd to the Pokemon world as a little girl.
    Join Dr. Fuji's apparently successful clone, as she explores this mishmash of Pokemon media and other creative liberties and grittier world.
    </Synopsis>
    <Genres>
        <Genre name="Drama" />
        <Genre name="Action" />
        <Genre name="Adventure" />
        <Genre name="Fantasy" />
    </Genres>
    <Tags>
        <Tag name="Reincarnation" />
        <Tag name="Portal Fantasy/Isekai" />
        <Tag name="Fan Fiction" />
        <Tag name="Female Lead" />
        <Tag name="Genetically Engineered" />
    </Tags>
    <Status>In Progress</Status>
    <DateCreated>$currentDate</DateCreated>
    <LastUpdated>$currentDate</LastUpdated>
    <Copyright>&#xA9; 2025 ChronicImmortality. All rights reserved.</Copyright>

    <!-- Optional: A list of chapters, primarily for defining order or a quick overview -->
    <Chapters>
"@

    foreach ($chapter in $chaptersInfo) {
        $titleEscaped = Escape-XML $chapter.Title
        $metadataXML += "`n        <Chapter ref=`"$($chapter.Number).xml`" title=`"$titleEscaped`" />"
    }
    
    $metadataXML += @"

        <!-- Add more Chapter elements as you write them -->
    </Chapters>
</StoryMetadata>
"@
    
    return $metadataXML
}

# Main script
# Get the parent directory (where the story folder should be)
$parentDir = Split-Path -Parent $PSScriptRoot
$sourceDir = Join-Path $parentDir "story"
$destDir = Join-Path $parentDir "pokemon-amber-xml"

Write-Host "Script running from: $PSScriptRoot"
Write-Host "Parent directory: $parentDir"
Write-Host "Source directory: $sourceDir"
Write-Host "Destination directory: $destDir"

# Create destination directory
if (!(Test-Path -Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

# Find all chapter markdown files
$chapterFiles = Get-ChildItem -Path $sourceDir -Filter "chapter*.md" | Sort-Object { Extract-ChapterNumber $_.Name }

if ($chapterFiles.Count -eq 0) {
    Write-Host "No chapter files found in $sourceDir"
    exit 1
}

$chaptersInfo = @()

Write-Host "Converting $($chapterFiles.Count) chapters..."

foreach ($file in $chapterFiles) {
    $chapterNum = Extract-ChapterNumber $file.Name
    
    Write-Host "Processing $($file.Name)..."
    
    # Extract title and content
    $extracted = Extract-TitleAndContent $file.FullName
    
    # Create XML chapter
    $xmlContent = Create-XMLChapter $extracted.Title $extracted.Content
    
    # Write XML file
    $outputFile = Join-Path $destDir "$chapterNum.xml"
    $xmlContent | Out-File -FilePath $outputFile -Encoding UTF8
    
    # Store chapter info for metadata
    $chaptersInfo += @{
        Number = $chapterNum
        Title = $extracted.Title
        Filename = "$chapterNum.xml"
    }
    
    Write-Host "  Created $chapterNum.xml"
}

# Create metadata file
Write-Host "Creating _meta.xml..."
$metadataXML = Create-MetadataXML $chaptersInfo

$metadataFile = Join-Path $destDir "_meta.xml"
$metadataXML | Out-File -FilePath $metadataFile -Encoding UTF8

Write-Host "`nConversion complete!"
Write-Host "Created $($chaptersInfo.Count) XML chapter files and _meta.xml in '$destDir' directory"
Write-Host "Chapters: $($chaptersInfo.Number -join ', ')" 