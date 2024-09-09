/*
 * Macro to split and rename channels from multiple series.  Should be able to work on individual tiff files too
 */
setBatchMode(true);
fs=File.separator; 

#@ File (label = "Input directory", style = "directory") input
#@ File (label = "Output directory", style = "directory") output
#@ String (label = "File suffix", value = ".tif") suffix

// See also Process_Folder.py for a version of this code
// in the Python scripting language.

processFolder(input);

// function to scan folders/subfolders/files to find files with correct suffix
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

function processFile(input, output, file) {
	// Do the processing here by adding your own code.
	// Leave the print statements until things work, then remove them.
	run("Bio-Formats Macro Extensions");
    Ext.setId(input + File.separator + file);
    Ext.getSeriesCount(seriesCount);
    sCount=seriesCount;
	//open(input + File.separator + file);
	folderName=substring(file,0,lastIndexOf(file, "."));
    condName=folderName;
    savePath=output+fs+folderName;

	for(l=1;l<=sCount;l++){
	   run("Bio-Formats Importer", "open=["+input + File.separator + file+"] autoscale color_mode=Default view=Hyperstack stack_order=XYCZT series_"+(l));
	   nameStore=getTitle();
	   getDateAndTime(year, month, dayOfWeek, dayOfMonth, hour, minute, second, msec);
	   print(hour+":"+minute+":"+second+" - Processing Series "+(l)+" of "+seriesCount);
	   //imageName=getInfo("image.filename");
	   //currentCount=l+1;
	   currentCount = l;
	   currentCount=d2s(currentCount,0);
	   currentLength=lengthOf(currentCount);
	   if(currentLength==1){
	      folderPath= condName+"-00"+currentCount+fs;
	   }
	   if(currentLength==2){
	      folderPath= condName+"-0"+currentCount+fs;
	   }
	   if(currentLength>=3){
	      folderPath= condName+currentCount+fs;
	   }
	fullsave=savePath+folderPath;
	File.makeDirectory(fullsave);
	
	print(folderPath);
	print(fullsave);
	//Ext.setId(fullsave);
	//run("Image Sequence... ","format=TIFF save=["+fullsave+"] name=["+condName+"]-");
	split_and_save(fullsave);
	run("Close All");
	
	}
}

function split_and_save(fullsave) {
	run("Split Channels");
	imgs = getList("image.titles");
	for (i = 0; i < imgs.length; i++) {
	   selectImage(imgs[i]);
	   run("Image Sequence... ","format=TIFF save=["+fullsave+"] name=["+imgs[i]+"_]-");
	   close(imgs[i]);
	}
}
