package projectReadFile;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;;

public class LeerArchivo {

	public static void main(String[] args) throws IOException 
	{
		Muestra_Contenido("D:\\yelp_academic_dataset_review.json");
	}
	
	public static void Muestra_Contenido(String archivo) throws FileNotFoundException, IOException
	{
		String cadena;
		FileReader fr = new FileReader(archivo);
		BufferedReader br = new BufferedReader(fr);
		int count = 0;
		
		//while((cadena = br.readLine())!=null)
		while((cadena = br.readLine())!=null && count<500)
		{
			count++;
			System.out.println(cadena);	
			System.out.println(count);
		}
		
		br.close();
	}

}
