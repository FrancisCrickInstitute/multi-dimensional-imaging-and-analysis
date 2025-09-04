/*
 * Macro to process multiple images in a folder
 * Split channels and z-planes and save individual images in a folder
 * 
 * requiered plugin: Bio-Format
 */
 
#@ File (label = "Source Folder", style = "directory") input
#@ File (label = "Save Folder", style = "directory") output
#@ String (label = "File suffix", value = ".") suffix

//setBatchMode("hide");
processFolder(input);

// Function to scan folders and subfolders for files with the correct suffix
function processFolder(input) {
	list = getFileList(input);
	list = Array.sort(list);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(input + File.separator + list[i]))
			processFolder(input + File.separator + list[i]);
		if(endsWith(list[i], suffix))
			processFile(input, output, list[i]);
	}
}

// Function to Split channels and  and save individual channels
function processFile(input, output, file) {
	run("Bio-Formats Windowless Importer", "open=["+ input + File.separator + file +"]");
	ImageTitle = File.nameWithoutExtension;
	run("Split Channels");
	if (nSlices > 1) {
		ImageDir = output + File.separator + ImageTitle;
		File.makeDirectory(ImageDir);
	}
	for (j=0;j<nImages;j++) {
        selectImage(j+1);
        title = getTitle;
        if (nSlices == 1) saveAs("tiff", output+File.separator+title);
        else {
        	suffix = "_";
        	run("Image Sequence... ", "dir=["+ImageDir+"] name=["+title+suffix+"] format=TIFF digits=2");
        }
	} 
	run("Close All");
	print("Processed "+ImageTitle+"");
}
