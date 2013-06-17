/********
Table Format:
Total URL: nURL
Total Class: nCLass 
At most classes Given: L 
URL  | 1st Cluster | 2nd Cluster | 3rd Cluster|....| L-th Cluster|
U1
U2
U3
.
.
.
UnURL
********/

createJASONChildren(int P, int l){ //create children for each class
	for( i=0 ; i<nURL ; i++){
		classFreq[Class[l]]++;
	}
	int *m = 1;
	child[0] = getMaxClass(classFreq[], m);
	
	int i = 0;
	
	while(i<nClass){
		i++;
		tempClass = getMaxClass(classFreq[],++*m);
		if(classFreq[level[i-1]] - classFreq[tempClass] < levelDiffThresrhold){
			child[i] = tempClass;
		}
		else{
			break;
		}
	}
	
	add all the links having Class id 0 to its parent P;
	for(j=0 ; j<i ; j++){
		create JASON node for child[j] and add to parent P;
		create seperate table for child[j];
		createJASONChildren(child[j],l+1);	
	}
}	



int getMaxClass(int classFreq[], int* m){ //gives the class having highest number of URL
		
	while(*m <= nClass){
	tempClass = nMax(classFreq[],*m);
		if(tempClass == 0){
			*m++;
			continue;
		}
		level = nMax(classFreq[],m);
		break;
	}
	return level;
}

int nMax(int arr[], int n){ //returns n-th maximum
//...
}

