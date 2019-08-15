import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the sherlockAndAnagrams function below.
    static int sherlockAndAnagrams(String s) {

    int len = 1;
    String mainString = s;
    //Create our hashmap object
    HashMap<String, Integer> hmap = new HashMap<String, Integer>();
    //while our mainString is longer that our length
    while (len < mainString.length()) {
        //This looks confusing but keepin mind that len,
        //is updated by the while loop and not the for loop
        for (int i = 0; i < mainString.length() - (len - 1); i++) {
            /*lets try to run a window across the array
            by grabbing the beginning*/
            String str = mainString.substring(i, i + len);
            //take our small grab and put it into array form
            char[] charArr = str.toCharArray();
            //sort the array
            Arrays.sort(charArr);
            //convert our array back to a string after sorting
            str = String.valueOf(charArr);
            //Check and add to map or increase value      
            if (hmap.containsKey(str)) {
                hmap.put(str, hmap.get(str) + 1);
            } else {
                hmap.put(str, 1);
            }
        }
    len++;
    }
    //System.out.println(hmap.keySet());
    System.out.println(hmap.values());
    //System.out.println(hmap.size());
    int anaCount = 0;
    int baseCount =0;
    //hmap.forEach(k,v) 
    for (Integer i : hmap.values()) {
        if (i >= 2) {
            //value * 2 - value all over 2 added up
            anaCount += (((i * i) - i) / 2);
            System.out.println(anaCount);
            }
        } 
    return(anaCount);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            int result = sherlockAndAnagrams(s);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
