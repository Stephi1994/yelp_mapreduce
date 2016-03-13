
        
        
         from functools import reduce

 # declaración de funciones
 def contar ( l ) :
 p = { }
 for x in l :
 		p.setdefault ( x , 0 )
 		p[ x ] += 1
 	return p

 def contar2 ( l , k ) :
 	p = { }
 	for i in range ( len ( l ) ) :
 		p.setdefault ( k [ i ] , { } )
 		p [k[i]] . setdefault (l[i] , 0 )
 		p [k[i]] [l[i]] += 1
 	return p

 def Pxik (atr , N, k ) :
 	if atr in N[ k ] :
 return N[ k ] [ a t r ] / Nk [ k ]
 	else :
 		return Nk [ k ] / n ∗∗ 2

 def classify ( t ) :
 	l = [ ( k , Nk [ k ] / n ∗
 		reduce (lambda x , y : x ∗ y ,
 			map( Pxik , t , Nxik ,
 		[ k for a in range ( len ( t ) ) ] ) ) )
 		for k in Nk. keys ( ) ]
 				return max( l , key=lambda x : x [ 1 ] ) [ 0 ]

 # carga del archivo
 l = list (map(lambda l : ( l . strip ( ) ) . split ( ’ , ’ ) ,
 	open ( ’mushroom.data.txt ’ , ’ r ’ ) . readlines ( ) ) )

 # construccion del training : 2 de cada 3
 train = l i s t (map(lambda x : x [ 1 ] ,
 	filter (lambda v : v [ 0 ] % 3 != 0 , enumerate ( l ) ) ) )
 n = len ( t r a in )

 # construcción del test : 1 de cada 3
 test = list (map(lambda x : x [ 1 ] ,
 	filter (lambda v : v [ 0 ] % 3 == 0 , enumerate ( l ) ) ) )

 # transpuesta del training
 m = list ( zip (∗ tra in ) )

# numerador de P ( k )
 Nk = contar (m[0])

 # numerador de P ( xi | k )
 Nxik = [ contar2 (m[ 1 ] , m[ 0 ] ) for i in range ( 1 , len (m) ) ]

 # clasificacion
 clases = list (map(lambda x : x . pop ( 0 ) , test ) )
 predicciones = list (map( classif y , test ) )

 # número de correctos
 print ( ’ Prec . : ’ , len ( list ( filter (lambda x : x [ 0 ] == x [ 1 ] ,
 		zip ( ∗ [ predicciones , clases ] ) ) ) )
 / len ( test ) ∗ 100, ’ %’ )
