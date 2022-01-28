class Solution {
    public int longestValidParentheses(String s) {
        Stack<Character> stack1 = new Stack<Character>();
        Stack<Character> stack2 = new Stack<Character>();
        int maxx=-1;
        int c1=0;
        int c2=0;
        for(char ch:s.toCharArray()){
            if (ch=='(')
            {
                stack1.push(ch);
                c1+=1;
                
            }
            else{
                if (!stack1.empty())
                {
                    stack1.pop();
                    if (stack1.empty())
                    {
                        maxx=Math.max(maxx,2*c1);
                    }
                }
                        
                else
                {
                    maxx=Math.max(maxx,2*c1);
                    c1=0;
                }
                        
                    
                }
            }
        
        // System.out.print(maxx);
        char[] chars = new StringBuilder(s).reverse().toString()
                            .toCharArray();
        for(char ch:chars)
        {
            if (ch==')')
            {
                stack2.push(ch);
                c2+=1;
                // System.out.print(stack2);
            }
            else{
                if (!stack2.empty())
                {
                    stack2.pop();
                    if (stack2.empty())
                    {
                        maxx=Math.max(maxx,2*c2);
                    }
                        
                }
                else
                {
                    maxx=Math.max(maxx,2*c2);
                    c2=0;
                }
                        
                    
                }
            }
        
        if (maxx==-1)
            return 0;
        return maxx;
        
    }
}