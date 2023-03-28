#include <iostream>
using namespace std;

struct cargo{
	int weight;
	int value;
};//注意這個分號

int main(){
	int amount;//儲存貨物數量
	while(cin>>amount){
		cargo data[amount];//儲存各貨物資訊
		for(int t=0; t<amount; t++)
			cin>>data[t].weight>>data[t].value;
		//DP的部分
		int space[101]={0};//儲存在各個容量下最大的價值 | 用101會比較方便因為會需要0的那格
		for(int object=0; object<amount; object++){
			for(int t2=100; t2-data[object].weight>=0; t2--){//注意如果是這種直接修改的作法需要由後向前，不然一個東西會被用很多次
                                            //就是這裡會用到容量0價值0的那格
				if(space[t2]<space[t2-data[object].weight]+data[object].value)
					space[t2]=space[t2-data[object].weight]+data[object].value;
			}
		}
		cout<<space[100]<<"\n";
	}
}
