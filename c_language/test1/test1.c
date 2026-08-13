#include <stdio.h>
int main(void){
	int a=0;
	int b = 0;
	int c = 0;
	int sales[5] = {8,15,12,5,20};
	int max_sales = sales[0]; // 첫 번째 값으로 초기화
	int max_index = 0;        // 첫 번째 인덱스(0)로 초기화
	for (int i=0; i < 5; i++) {
		a += sales[i];
	}
	printf("전체 판매 수량: %d\n", a);
	printf("평균 판매 수량: %.1f\n", a / 5.0);
	for (int i=0; i < 5; i++) {
		if (sales[i] >= 10) {
			b++;
		}
	}
	printf("10개 이상 판매 상품 수: %d\n", b);
	for (int i=0; i < 5; i++) {
		if (sales[i] < a/5.0) {
			c++;
		}
	}
	printf("평균 미만 상품 수: %d\n", c);
	for (int i = 1; i < 5; i++) {
		if (sales[i] > max_sales) {
			max_sales = sales[i]; // 더 큰 값을 만나면 갱신
			max_index = i;        // 그때의 인덱스 저장
		}
	}
	printf("최고 판매 수량: %d\n", max_sales);
	printf("최고 판매 번호: %d번", max_index + 1);
    //int total = 0;       // 전체 수량
    //int over_10 = 0;     // 10개 이상 판매 상품 수
    //int below_avg = 0;   // 평균 미만 상품 수

    //int max_sales = sales[0]; // 최고 판매 수량
    //int max_num = 1;          // 최고 판매 번호 (1부터 시작)

    //// 1. 전체 수량 및 최고 판매 수량/번호 구하기
    //for (int i = 0; i < 5; i++) {
    //    total += sales[i];

    //    if (sales[i] > max_sales) {
    //        max_sales = sales[i];
    //        max_num = i + 1; // 판매 번호는 1부터 시작하므로 인덱스에 +1
    //    }
    //}

    //// 2. 평균 수량 계산
    //double average = (double)total / 5.0;

    //// 3. 10개 이상 판매 상품 수 및 평균 미만 상품 수 구하기
    //for (int i = 0; i < 5; i++) {
    //    if (sales[i] >= 10) {
    //        over_10++;
    //    }
    //    if (sales[i] < average) {
    //        below_avg++;
    //    }
    //}

    //// 결과 출력
    //printf("전체 판매 수량: %d\n", total);
    //printf("평균 판매 수량: %.1f\n", average);
    //printf("10개 이상 판매 상품 수: %d\n", over_10);
    //printf("최고 판매 수량: %d (판매 번호: %d번)\n", max_sales, max_num);
    //printf("평균 미만 상품 수: %d\n", below_avg);
	return 0;
}