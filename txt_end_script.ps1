$files = Get-ChildItem "" #directory where you want to change file extension

foreach ($f in $files){
    $outfile = $f.FullName 
    $fileName = $f.Name

    if ($fileName -Like "*.txt")
    {
          #do nothing

    } 
    else
    {
        $newName = $fileName + ".txt"        
        Rename-Item -Path $outfile -NewName $newName

    }      

} # end of for loop