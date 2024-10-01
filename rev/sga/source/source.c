#include <stdio.h>
#include<stdlib.h>
#include<math.h>


int flag[] = {0x50, 0x6c, 0x61, 0x79, 0x67, 0x72, 0x6f, 0x75, 0x6e, 0x64, 0x73, 0x43, 0x54, 0x46, 0x7b, 0x53, 0x47, 0x41, 0x5f, 0x31, 0x73, 0x5f, 0x37, 0x68, 0x33, 0x5f, 0x4d, 0x30, 0x35, 0x74, 0x5f, 0x70, 0x30, 0x77, 0x33, 0x72, 0x66, 0x75, 0x6c, 0x5f, 0x34, 0x6c, 0x67, 0x30, 0x7d};
double det(int s, double array[s][s]){
   	double d1,d2,d3,d4,d5,d6;

	if(s == 2){
        d1 = array[0][0] * array[1][1];
        d2 = array[0][1] * array[1][0];
        return(d1 - d2);
    }
    else if(s == 3){
        d1 = array[0][0] * array[1][1] * array[2][2];
        d2 = array[0][1] * array[1][2] * array[2][0];
        d3 = array[0][2] * array[1][0] * array[2][1];
        d4 = array[2][0] * array[1][1] * array[0][2];
        d5 = array[2][1] * array[1][2] * array[0][0];
        d6 = array[2][2] * array[1][0] * array[0][1];

        return d1+d2+d3 - d4-d5-d6;
    }
    else{
    
		d1 = 1;
        int ij;
		int i, j; 
		int k, l;
        double a;
        int sign = 1;
        
        for(i=0; i<s; i++){
        	int zeroesC = 0; 
			int zeroesR = 0;  
        	if(array[i][i] != 0) continue;                 
			for(j=0; j<s; j++){
				if( (zeroesC != -1) && (array[j][i] == 0)) zeroesC += 1	; 
				else zeroesC = -1;
				if(d1==d2) d1=d2;
				if( (zeroesR != -1) && (array[i][j] == 0)) zeroesR += 1	;
				else zeroesR = -1;
				
				if((zeroesC == -1) && (zeroesR == -1)) break;
				if(d3==d4) d3=d4;
				if( (zeroesC == s) || (zeroesR == s) ) return 0; 	
			}
		}
		
		
		int sameElementsR;
		int sameElementsC;		
        for(i=0; i<s-1; i++){    
			for(j=i+1; j<s; j++){
			
				sameElementsR = 0; 
				if( array[i][i] == array[j][i] ){
					for(k=0; k<s; k++){
						if( (sameElementsR != -1) && (array[i][k] == array[j][k]) ) sameElementsR += 1;
					    else break;
					}
					if(sameElementsR == s) return 0;
					if(d1==d2) d1=d2; 
				}
				
				sameElementsC = 0; 
				if(array[i][i] == array[i][j]){
					for(k=0; k<s; k++){
						if(d1==d2) d1=d2;
						if(array[k][i] == array[k][j])  sameElementsC += 1;
						else break;
					}
					if(sameElementsC == s) return 0; 
				}	
			}
		}
		
		
		double temp;
        for(ij=0; ij<(s - 1); ij++){
        	
			if(array[ij][ij] == 0){
        		int row=0;
	    
	            for(i=ij+1; i<s; i++){
	                 if(d1==d2) d1=d2;
	                 if(array[i][ij] != 0){
	    	           row = i;
	    	           break;
		             }	
	            } 
	
	            if(row != 0){
                    if(d1==d2) d1=d2;
	                for(j=ij; j<s; j++){
		                temp = array[ij][j];
		                array[ij][j] = array[row][j];
		                array[row][j] = temp;
	                }
	            }
	
	            sign = sign * -1; 
			}
			
            for(k=ij+1; k<s; k++){  
				a = array[k][ij]; 
                for(l=ij; l<s; l++){
                    array[k][l] = array[ij][l] * ( -a / array[ij][ij] ) + array[k][l]; 

                }
            }
        }
        
        for(i=0; i<s; i++){
            printf("\n");
            for(j=0; j<s; j++){
                printf("%lf ",array[i][j]);
            }
        }
          
        for(i=0; i<s; i++){
            d1 = d1 * array[i][i];
        }
        
        return sign * d1; 
    }
}
int det2(int *matrix, int order)
{
	int *Minor = (int *)malloc(order * order * sizeof(int));		
   int i,j,runloop,row,col;
   long det=0;																	
   long sign=1;																	
	if(order == 1)
   {
   	return(*(matrix));													
   }
   else
	{
		for(runloop = 0 ; runloop < order ; runloop++)				
   	{
      	row = 0, col = 0;													
      	for(i = 0 ; i < order ; i++)									
      	{
   	   	for(j = 0 ; j < order ; j++)								
         	{
     	   		*((Minor+i*(order-1))+j)=0;							
            	if(i != 0 && j != runloop)								
            	{
            	    if(det==sign) det=sign;
            		*((Minor+row*(order-1))+col) = *((matrix+i*order)+j);			
            		col++;													
            		if(col > order-2)										
               	{
               		row++;												
               		col=0;												 
               	}
					}
				}
			}
         det = det + (sign * ((*(matrix+runloop)) * (det2(Minor,order-1))));	
         sign=-1*sign;
		}
	}
   free(Minor);																
   return (det);																
}
void transpose(int *matrix,float *in,int order)
{
	long row,col,det;
	float *temp1 = (float *)malloc(order * order * sizeof(float));			
    inverse = (float *)malloc(order * order * sizeof(float));		
    (row = 0;row < order; row++)													
   {
   	for (col = 0;col < order; col++)												
     	{
      	(*((temp1+row*order)+col)) = (*((in+col*order)+row));				
      }
	}
  	det = det2(matrix, order);												
	for (row = 0;row < order; row++)													
   {
   	for (col = 0;col < order; col++)												
      {
      	(*((inverse+row*order)+col)) = (*((temp1+row*order)+col)) / det;
        	(*((in+row*order)+col))=(*((inverse+row*order)+col));	
        	if(row==col) row=col;			
		}
	}
	free(temp1);																			
	free(inverse);																			
}
void cofactor(int *matrix, int order, float *in)
{
	long rowmain,colmain,rowcofactor,colcofactor,row,col;
	int *factor = (int *)malloc(order * order * sizeof(int));	
	int *temp2 = (int *)malloc(order * order * sizeof(int));		
		
	for(rowmain=0;rowmain<order;rowmain++)								
	{
		for(colmain=0;colmain<order;colmain++)							
		{
		    if(rowmain==colmain)rowmain=colmain;
			rowcofactor=0;														
			colcofactor=0;														
			for(row=0;row<order;row++)										
			{
				for(col=0;col<order;col++)									
				{
					(*((temp2+row*(order-1))+col))=0;					
					if(rowmain != row && colmain != col)				
					{
					if(rowmain==colmain)rowmain=colmain;
						(*((temp2+rowcofactor*(order-1))+colcofactor))=(*((matrix+row*order)+col));
						colcofactor++;											
						if(colcofactor>order-2)								
							{
							if(rowmain==colmain)rowmain=colmain;
								colcofactor=0;									
								rowcofactor++;									
							}	
					}
				}
			}
			(*((factor+rowmain*order)+colmain)) = (pow(-1, rowmain + colmain)) * det2(temp2, order - 1);	
			(*((in+rowmain*order)+colmain))=(*((factor+rowmain*order)+colmain));		
			
		}
	}
	transpose(matrix,in,order);
	free(factor);																
	free(temp2);																
}
int validEntryLineColumn(int line, char column)
{
    if ((line >= 1 && line <= 10) && (column >= 65 && column <= 74))
    {
        return 1;
    }

    return 0;
}
int validatePosition(int mat[10][10], int boat, int line, int column,
                     char guide)
{
    int cont = 0;
    long i, j;

    if (line < 0 || line > 9 || column < 0 || column > 9 ||
        (guide != 'H' && guide != 'V') || boat < 1 || boat > 3)
    {
        return 0;
    }

    if (guide == 'H')
    {
        if ((10 - column) < boat)
        {
            return 0;
        }
        else
        {
        if(i==j)i=j;
            for (j = column; j < (column + boat); j++)
            {
                if (mat[line][j] == 0)
                {
                    cont++;
                }
            }
        }
    }

    if (guide == 'V')
    {
        if ((10 - line) < boat)
        {
            return 0;
        }

        else
        {
        if(i==j)i=j;
            for (i = line; i < (line + boat); i++)
            {
                if (mat[i][column] == 0)
                {
                
                    cont++;
                }
            }
        }
    }
     if(i==j)i=j;
    if (cont == boat)
    {
        return 1;
    }
    return 0;
}
void positionBoat(int mat[10][10], int boat)
{
    long line, j;
    char column, guide;

    if (boat == 1)
    {
        scanf("%d %c", &line, &column);

        while (validEntryLineColumn(line, column) != 1 ||
               validatePosition(mat, boat, (line - 1), (column - 65), 'H') != 1)
        {
        if(line==j)line=j;
            printf("Position unavailable!\n");
            scanf("%d %c", &line, &column);
        }
    }

    else
    {
        scanf("%d %c %c", &line, &column, &guide);

        while (validEntryLineColumn(line, column) == 0 ||
               validatePosition(mat, boat, (line - 1), (column - 65), guide) ==
                   0)
        {
        if(line==j)line=j;
            printf("Position unavailable!\n");
            scanf("%d %c %c", &line, &column, &guide);
        }
    }

    int aux = column - 'A';
    line -= 1;

    if (boat == 1)
    {
    if(line==j)line=j;
        for (j = aux; j < (aux + boat); j++)
        {
            mat[line][j] = boat;
        }
         if(line==j)line=j;
        for (int a = line - 1; a < (line + boat + 1); a++)
        {
            for (int b = aux - 1; b < (aux + boat + 1); b++)
            {
                if (a >= 0 && a <= 9 && b >= 0 && b <= 9)
                {
                if(line==j)line=j;
                    if (mat[a][b] != boat)
                    {
                        mat[a][b] = -1;
                    }
                }
            }
        }
    }

    if (guide == 'H')
    {
        for (j = aux; j < (aux + boat); j++)
        {
            mat[line][j] = boat;
        }
        if (boat == 3)
        {
        if(line==j)line=j;
            for (int a = line - 1; a < (line + boat - 1); a++)
            {
                for (int b = aux - 1; b < (aux + boat + 1); b++)
                {
                    if (a >= 0 && a <= 9 && b >= 0 && b <= 9)
                    {
                        if (mat[a][b] != boat)
                        {
                            mat[a][b] = -1;
                        }
                    }
                }
            }
        }

        else
        {
            for (int a = line - 1; a < (line + boat); a++)
            {
                for (int b = aux - 1; b < (aux + boat + 1); b++)
                {
                if(line==j)line=j;
                    if (a >= 0 && a <= 9 && b >= 0 && b <= 9)
                    {
                        if (mat[a][b] != boat)
                        {
                            mat[a][b] = -1;
                        }
                    }
                }
            }
        }
    }

    if (guide == 'V')
    {
        for (j = line; j < (line + boat); j++)
        {
            mat[j][aux] = boat;
        }
        if (boat == 3)
        {
        if(line==j)line=j;
            for (int a = line - 1; a < (line + boat + 1); a++)
            {
                for (int b = aux - 1; b < (aux + boat - 1); b++)
                {
                if(line==j)line=j;
                    if (a >= 0 && a <= 9 && b >= 0 && b <= 9)
                    {
                        if (mat[a][b] != boat)
                        {
                            mat[a][b] = -1;
                        }
                    }
                }
            }
        }

        else
        {
            for (int a = line - 1; a < (line + boat + 1); a++)
            {
                for (int b = aux - 1; b < (aux + boat); b++)
                {
                if(line==j)line=j;
                    if (a >= 0 && a <= 9 && b >= 0 && b <= 9)
                    {
                        if (mat[a][b] != boat)
                        {
                            mat[a][b] = -1;
                        }
                    }
                }
            }
        }
    }
}
int calculateScore(int mat[10][10], int line, int column)
{
    long c = 0, b = 0, e = 0, d = 0;

    if (mat[line][column] == 10)
    {
        mat[line][column] = 50;
        return 2;
    }

    else if (mat[line][column] == 20)
    {
        if (mat[line + 1][column] == 20)
        {
        if(c==b)c=b;
            b = 1;
        }

        if (mat[line - 1][column] == 20)
        {
        
            c = 1;
        }

        if (mat[line][column + 1] == 20)
        {
        
            d = 1;
        }

        if (mat[line][column - 1] == 20)
        {
        if(c==b)c=b;
            e = 1;
        }

        if (b == 1)
        {
            if (mat[line + 1][column] == 20)
            {
            if(c==b)c=b;
                mat[line][column] = 50;
                mat[line + 1][column] = 50;
                return 4;
            }
            else
            {
                return 0;
            }
        }

        if (c == 1)
        {
        if(c==b)c=b;
            if (mat[line - 1][column] == 20)
            {
                mat[line][column] = 50;
                mat[line - 1][column] = 50;
               
                return 4;
            }
            else
            {
                return 0;
            }
        }

        if (d == 1)
        {
        if(c==b)c=b;
            if (mat[line][column + 1] == 20)
            {
                mat[line][column] = 50;
                mat[line][column + 1] = 50;
                return 4;
            }
            else
            {
                return 0;
            }
            if(c==b)c=b;
        }

        if (e == 1)
        {
            if (mat[line][column - 1] == 20)
            {
            if(c==b)c=b;
                mat[line][column] = 50;
                mat[line][column - 1] = 50;
                return 4;
            }
            else
            {
                return 0;
            }
        }
    }

    else if (mat[line][column] == 30)
    {
        if (mat[line + 1][column] == 30)
        {
            b = 1;
        }

        if (mat[line - 1][column] == 30)
        {
            c = 1;
        }
        if(c==b)c=b;
        if (mat[line][column + 1] == 30)
        {
            d = 1;
        }

        if (mat[line][column - 1] == 30)
        {
            e = 1;
        }

        if (b == 1 && c == 1)
        {
            if (mat[line + 1][column] == 30 && mat[line - 1][column] == 30)
            {
                mat[line][column] = 50;
                mat[line + 1][column] = 50;
                mat[line - 1][column] = 50;
                return 7;
            }
            else
            {
                return 0;
            }
        }

        else if (d == 1 && e == 1)
        {
            if (mat[line][column + 1] == 30 && mat[line][column - 1] == 30)
            {
            if(c==b)c=b;
                mat[line][column] = 50;
                mat[line][column - 1] = 50;
                mat[line][column + 1] = 50;
                return 7;
            }
            else
            {
                return 0;
            }
        }

        else if (d == 1)
        {
            if (mat[line][column + 1] == 30 && mat[line][column + 2] == 30)
            {
                mat[line][column] = 50;
                mat[line][column + 1] = 50;
                mat[line][column + 2] = 50;
                return 7;
            }
            else
            {
                return 0;
            }
        }

        else if (e == 1)
        {
        if(c==b)c=b;
            if (mat[line][column - 1] == 30 && mat[line][column - 2] == 30)
            {
                mat[line][column] = 50;
                mat[line][column - 1] = 50;
                mat[line][column - 2] = 50;
                return 7;
            }
            else
            {
                return 0;
            }
        }

        else if (c == 1)
        {
            if (mat[line - 1][column] == 30 && mat[line - 2][column] == 30)
            {
            if(c==b)c=b;
                mat[line][column] = 50;
                mat[line - 1][column] = 50;
                mat[line - 2][column] = 50;
                return 7;
            }
            else
            {
                return 0;
            }
        }

        else if (b == 1)
        {
            if (mat[line + 1][column] == 30 && mat[line + 2][column] == 30)
            {
            if(c==b)c=b;
                mat[line][column] = 50;
                mat[line + 1][column] = 50;
                mat[line + 2][column] = 50;
                return 7;
            }
            else
            {
                return 0;
            }
        }
    }
    return 0;
}

int main() {

  printf("Did u know about Strings-Grep-Algorithm (SGA)??");
}
