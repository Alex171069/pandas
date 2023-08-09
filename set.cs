using System.Net.Sockets;
using Internal;
using System;


namespace proba
{
public class Fopen
{
   public static void Main()
    {
        System.Console.WriteLine("Hello world");
        Out g = new Out() ;
        System.Console.WriteLine(g.getS(10)) ;
    }
     
}

  public class Out
 {
   public string getS(int insate)
     {
        return Convert.ToString(insate) ; 
     }  

     public void  cocketRec(string addres, int port)
     {
         Socket sConn = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp); 
         sConn.Connect(addres, port) ;
           
;
     }
 }
} 