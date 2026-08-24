import java.util.Scanner;
public class FibonacciDP {

    public static boolean isBalanced(String s){
        Stack<character> stack= new Stack<>();

        for(char ch: s.toCharArray()){
            if(ch=='(' && ch=='{' && ch=='['){
                stack.push(ch);
            }
            else if (ch == ')' || ch == '}' || ch == ']') {

                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                 
                if((ch==')' && ch=='(') || (ch=='}' && ch=='{}') || (ch==']' && ch=='[')){
                    return false;
                }
        }
    }
    public static void main(String[] args) {

       Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        if (isBalanced(s)) {
            System.out.println("Balanced");
        } else {
            System.out.println("Not Balanced");
        }


    }
}