import java.util.*;
import java.util.Scanner;
import java.util.ArrayList;
public class wocao{
	public static void main(String[] args) {
/*		Scanner s = new Scanner(System.in);

		if(s.nextInt()<=100 && s.nextInt() >=50){
			System.out.println("wo an le yi xia");
		}else{
			System.out.println("tuichu");
		}
*/
		System.out.println("asdfasdfasasdfasfasfsafasfsfasfas");
		int a[] = {1,2,3,4,5,6,7,8,9,0,11,22,33,44,55,66,77,88,99,999,888,777,666,555,444,333,222,111};
		Maopao(a);
		ArrayList<String> list  new ArrayList<String>();
	}

	public static void Maopao(int a[]){

		System.out.println("排序前：");
		for (int i= 0; i<a.length; i++) {
			if (i == a.length-1) {
				System.out.println(a[i]);
			}else{
				System.out.print(a[i]+",");	
			}
			
		}

		System.out.println("排序后：");
		for (int i=0; i<a.length; i++) {
			for (int j=i+1; j<a.length; j++) {
				int temp;
				if (a[i]<a[j]) {
					temp = a[i];
					a[i] = a[j];
					a[j] = temp;
				}
			}
			if (i == a.length-1) {
				System.out.println(a[i]);
			}else{
				System.out.print(a[i]+",");	
			}
		}
	}
}
