class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set() 
        
        for email in emails:
            emailSplitted = email.split("@")
            

            if "+" in emailSplitted[0]:
                emailSplitted[0] = emailSplitted[0].split("+")[0]
                
            emailSplitted[0] = emailSplitted[0].replace(".", "")

            emailRejoined = f"{emailSplitted[0]}@{emailSplitted[1]}"
            output.add(emailRejoined)

        return len(output)
