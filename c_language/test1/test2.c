#include <stdio.h>
int main(void) {
	int total = 0;
	int ten = 0;
	float reber = 0;
	int indexe = 0;
	int low = 0;
	int lowdx = 0;
	int sales[5] = { 8,15,12,5,20 };
	int a = sales[0];
	int hi = sales[0];
	for (int i=0; i < 5; i++) {
		total += sales[i];
		if (10 <= sales[i])
			ten++;
	}
	reber = total / 5.0;
	for (int i=0; i < 5; i++) {
		if (hi < sales[i]) {
			hi = sales[i];
			indexe = i;
		}
		if (sales[i] < reber)
			low++;
	}

	for (int i = 0; i < 5; i++) {
		if (a > sales[i]) {
			a = sales[i];
			lowdx = i;
		}
		if (sales[i] == 0)
			printf("품절입니다");
	}
	printf("전체 판매 수량: %d\n", total);
	printf("평균 판매 수량: %.1f\n", reber);
	printf("10개 이상 판매 상품 수: %d\n", ten);
	printf("최고 판매 수량: %d\n", hi);
	printf("최저 판매 수량: %d\n", a);
	printf("최고 판매 상품 번호: %d\n", indexe+1);
	printf("최저 판매 상품 번호: %d\n", lowdx + 1);
	printf("평균 미만 판매 수량: %d", low);

    //int totalSales = 0;
    //int tenOrMoreCount = 0;
    //float average = 0;
    //int belowAverageCount = 0;

    //int sales[5] = { 8, 15, 12, 5, 20 };

    //// 최고/최저 수량 및 인덱스 초기화
    //int maxSales = sales[0];
    //int maxIndex = 0;
    //int minSales = sales[0];
    //int minIndex = 0;

    //// 1단계: 전체 판매 수량 합산 및 10개 이상 판매 수 카운트
    //for (int i = 0; i < 5; i++) {
    //    totalSales += sales[i];
    //    if (sales[i] >= 10) {
    //        tenOrMoreCount++;
    //    }
    //}

    //// 평균 계산
    //average = totalSales / 5.0;

    //// 2단계: 최고/최저 수량, 평균 미만 개수, 품절 여부 확인
    //for (int i = 0; i < 5; i++) {
    //    // 최고 판매 수량 및 번호 갱신
    //    if (maxSales < sales[i]) {
    //        maxSales = sales[i];
    //        maxIndex = i;
    //    }

    //    // 최저 판매 수량 및 번호 갱신
    //    if (minSales > sales[i]) {
    //        minSales = sales[i];
    //        minIndex = i;
    //    }

    //    // 평균 미만 판매 상품 수 카운트
    //    if (sales[i] < average) {
    //        belowAverageCount++;
    //    }

    //    // 품절 상품 체크 (0개일 때)
    //    if (sales[i] == 0) {
    //        printf("%d번 상품은 품절입니다!\n", i + 1);
    //    }
    //}

    //// 결과 출력
    //printf("\n--- 판매 통계 결과 ---\n");
    //printf("전체 판매 수량: %d\n", totalSales);
    //printf("평균 판매 수량: %.1f\n", average);
    //printf("10개 이상 판매 상품 수: %d\n", tenOrMoreCount);
    //printf("최고 판매 수량: %d\n", maxSales);
    //printf("최저 판매 수량: %d\n", minSales);
    //printf("최고 판매 상품 번호: %d번\n", maxIndex + 1);
    //printf("최저 판매 상품 번호: %d번\n", minIndex + 1);
    //printf("평균 미만 판매 수량: %d\n", belowAverageCount);
	return 0;
}