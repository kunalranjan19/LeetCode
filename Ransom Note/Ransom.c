bool canConstruct(char * ransomNote, char * magazine){
      bool ans = true;
    char *loc;
    for(int i=0;i<strlen(ransomNote); i++){
        if(strchr(magazine, ransomNote[i])){
            loc = strchr(magazine,ransomNote[i]);
            *loc = '0';
        }else{
            ans = false;
        }
    }
    
    return ans;

}