//헤더파일: 공통적으로 참조할 내용 선언
// #pragma once //중복 읽기 방지

#ifndef EXCHANGE_H  //정의되어 있지 않으면
#define EXCHANGE_H  //EXCHANGE_H 만든다

// 1. 환율 설정 (1달러당 원화 가격)
#define RATE  1600.0 //기호상수 선언

// 2. 함수 선언
double won(double usd);  // 달러를 원화로 변환
double doll(double krw); // 원화를 달러로 변환
#endif