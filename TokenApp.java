package projectReadFile;

import java.io.IOException;
import java.util.StringTokenizer;

public class TokenApp {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		String nombre ="text: Angel Franco García";
		StringTokenizer tokens = new StringTokenizer(nombre, "text" );
		while (tokens.hasMoreTokens())
		{
			System.out.println(tokens.nextToken());
		}
		

	}

}
