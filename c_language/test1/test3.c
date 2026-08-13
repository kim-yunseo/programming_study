#include<stdio.h>
int main() {
	int sales[5] = { 8,15,12,5,20 };
	int sum = 0;
	int ten = 0;
	int hi = 0;
	int ralo = 0;
	int hidx = 0;
	int lo = sales[0];
	int lodx = 0;
	for (int i = 0; i < 5; i++) {
		sum += sales[i];
		if (sales[i] >= 10)
			ten++;
		if (hi < sales[i]) {
			hi = sales[i];
			hidx = i;
		}
		if (lo > sales[i]) {
			lo = sales[i];
			lodx = i;
		}
		if (sales[i] == 0)
			printf("품절되었습니다.");
	}
	for (int i = 0; i < 5; i++) {
		if (sales[i] < sum / 5.0)
			ralo++;
	}
	
	printf("전체 판매 수량: %d\n", sum);
	printf("평균 판매 수량: %.1f\n", sum/5.0);
	printf("10개 이상 판매 상품 수: %d\n", ten);
	printf("최고 판매 수량: %d\n", hi);
	printf("최고 판매 상품 번호: %d\n", hidx+1);
	printf("최저 판매 수량: %d\n", lo);
	printf("최저 판매 상품 번호: %d\n", lodx+1);
	printf("평균 미만 판매 수량: %d\n", ralo);
	
	return 0;
}