#include <stdio.h> 
#include <string.h> 
#include <math.h> 
#include <omp.h> 
#include <stdlib.h>

#define         X_RESN  1080     /* x resolution */ 
#define         Y_RESN  1080     /* y resolution */ 
#define         X_MIN   -2.0 
#define         X_MAX    2.0 
#define         Y_MIN   -2.0 
#define         Y_MAX    2.0 
typedef unsigned char pixel_t[3];
typedef struct complextype 
        { 
        float real, imag; 
        } Compl; 
int main ( int argc, char* argv[]) 
{ 
        /* Mandlebrot variables */ 
        int    i, j, k; 
        Compl  z, c; 
		FILE * fp;
        float  lengthsq, temp; 
		//printf("hi");
		pixel_t *pixels = malloc(sizeof(pixel_t)*Y_RESN*X_RESN);
		//printf("hi");
        int    maxIterations, nthreads; 
        int    res[X_RESN][Y_RESN];  
        double start_t, end_t; 
        /* Get number of iterations and threads */ 
        maxIterations = atoi( argv[1] ); 
        nthreads = atoi( argv[2] ); 
        omp_set_num_threads(nthreads); 
        /* Start  timing */ 
        start_t = omp_get_wtime();          
		#pragma omp parallel for shared(res,maxIterations,pixels) private(i,j,z,c,k,temp,lengthsq) schedule(dynamic)
		for(i=0; i < Y_RESN; i++)		
		for(j=0; j < X_RESN; j++)
		{ 
        	z.real = z.imag = 0.0; 
        	c.real = X_MIN + j * (X_MAX - X_MIN)/X_RESN; 
        	c.imag = Y_MAX - i * (Y_MAX - Y_MIN)/Y_RESN; 
        	k = 0; 
        	do 
			{    /* iterate for pixel color */ 
            	temp = z.real*z.real - z.imag*z.imag + c.real; 
            	z.imag = 2.0*z.real*z.imag + c.imag; 
            	z.real = temp; 
            	lengthsq = z.real*z.real+z.imag*z.imag; 
            	k++; 
        	} while (lengthsq < 4.0 && k < maxIterations); 
        	if(k == maxIterations)
            {
                    //color(0, 0, 0); // black
            	pixels[i*X_RESN+j][0] = 0;
            	pixels[i*X_RESN+j][1] = 0;
            	pixels[i*X_RESN+j][2] = 0;
            }
            else
            {
                   // double z = sqrt(newRe * newRe + newIm * newIm);
                    //int brightness = 256 * log2(1.75 + i - log2(log2(z))) / log2((double)ITERATIONS);

                                    //color(brightness, brightness, 255)
            	pixels[i*X_RESN+j][0] = 255;
            	pixels[i*X_RESN+j][1] = 255;
            	pixels[i*X_RESN+j][2] = 255;
            }
		}
        /* End timing */ 
        end_t = omp_get_wtime(); 
        printf("%f %d", end_t-start_t,   
                 nthreads); 
		fp= fopen("MandelbrotSet.ppm","wb");

		fprintf(fp, "P6\n# CREATOR: Saumya J. Weeks / mandel program\n");
        fprintf(fp, "%d %d\n255\n", X_RESN, Y_RESN);

        //fprintf(fp,"P6\n %s\n %d\n %d\n %d\n","# no comment",ImageWidth,ImageHeight,MaxColorComponentValue);
          int   yactual=0;
           int xactual=0;
        for(yactual=0;yactual<Y_RESN; yactual++)
            for( xactual=0; xactual<X_RESN; xactual++)
                fwrite(pixels[yactual*X_RESN + xactual],1,sizeof(pixel_t),fp);
        fclose(fp);

            free(pixels);
        /* End of program */ 
        return 0; 
}
