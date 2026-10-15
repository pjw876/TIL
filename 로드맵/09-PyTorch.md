---
start: 2026-11-19
perday: 1
---
# 09. PyTorch 로드맵 (11일)

- **목표**: 학습 루프를 직접 짜고, 트랜스포머 구조를 이해하고, 사전학습 모델을 불러 파인튜닝까지
- **하루**: 120분 (주제 2개 × 60분)
- **선행**: 07-수학 Day 4~7(경사하강법·역전파), 08-ML기초 Day 1~7
- **자료**: PyTorch 공식 튜토리얼(Learn the Basics), Karpathy *Neural Networks: Zero to Hero*(nanoGPT), Hugging Face NLP/LLM Course
- **환경**: GPU 없으면 Google Colab 사용
- **TIL 카테고리**: `AI/`

---

## Day별 계획

- [ ] **Day 1** — 텐서 기초 + 연산 감각
  - **텐서 기초**: shape, dtype, device, numpy와 변환
  - **연산 감각**: 브로드캐스팅, 인덱싱, `reshape/view/permute`
    확인: `view`와 `reshape`의 차이는?
- [ ] **Day 2** — autograd + `nn.Module`
  - **autograd**: `requires_grad`, `backward()`, `no_grad`, 그래디언트 누적 확인
  - **`nn.Module`**: 선형회귀를 `nn.Linear`로 구현, 파라미터 확인
- [ ] **Day 3** — 학습 루프 5단계 + Dataset / DataLoader
  - **학습 루프 5단계**: `forward → loss → zero_grad → backward → step`을 **외워서** 작성
    확인: `zero_grad()`를 빼면 어떻게 되나?
  - **Dataset / DataLoader**: 커스텀 Dataset, batch, shuffle, `num_workers`
- [ ] **Day 4** — 복습 + 미니 + 활성화, 초기화, 정규화 계층
  - **복습 + 미니**: MNIST를 MLP로 분류, 정확도 97%+ 목표
  - **활성화, 초기화, 정규화 계층**: ReLU/GELU, BatchNorm/LayerNorm, Dropout
- [ ] **Day 5** — 옵티마이저와 스케줄러 + 검증과 체크포인트
  - **옵티마이저와 스케줄러**: SGD/Adam/AdamW, LR 스케줄러, warmup
  - **검증과 체크포인트**: 검증 루프(`model.eval()`), early stopping, `state_dict` 저장/로드
    확인: `model.eval()`과 `torch.no_grad()`는 각각 무엇을 바꾸나?
- [ ] **Day 6** — GPU와 혼합정밀도 + CNN 기본
  - **GPU와 혼합정밀도**: `.to(device)`, `torch.autocast`, 메모리 사용량 확인
  - **CNN 기본**: CIFAR-10 분류, 컨볼루션 직관
- [ ] **Day 7** — 학습 디버깅 + 복습 + 미니
  - **학습 디버깅**: **한 배치 과적합 테스트**, loss NaN 원인, 그래디언트 확인
  - **복습 + 미니**: 학습 곡선(train/val loss) 그래프와 해석을 TIL로
- [ ] **Day 8** — 토크나이저와 임베딩 층 + RNN/LSTM → Attention
  - **토크나이저와 임베딩 층**: BPE 직관, `nn.Embedding`, 토큰 수 세기
    연결: LLM 비용/컨텍스트 한계가 토큰 단위인 이유
  - **RNN/LSTM → Attention**: RNN의 한계, attention이 필요한 이유
- [ ] **Day 9** — self-attention 직접 구현 + 트랜스포머 블록
  - **self-attention 직접 구현**: Q, K, V, scaled dot-product, 마스킹
    확인: 왜 `sqrt(d_k)`로 나누나?
  - **트랜스포머 블록**: multi-head, residual, LayerNorm, FFN → 작은 GPT 학습 (nanoGPT 따라가기)
- [ ] **Day 10** — Hugging Face로 추론 + LoRA 맛보기
  - **Hugging Face로 추론**: `transformers`로 사전학습 모델 로드, 토크나이저, 생성 파라미터(temperature, top_p)
  - **LoRA 맛보기**: `peft`로 어댑터 붙이기, 학습 파라미터 수 비교
    확인: LoRA가 메모리를 아끼는 원리 한 문장
- [ ] **Day 11** — 최종 미니
  - **최종 미니**: 한국어 감성 분류 모델 파인튜닝 + **평가 리포트**(지표, 오류 분석, 한계)를 README로

---

## 이 정도면 점검 끝

- [ ] 학습 루프를 보지 않고 쓰고 각 줄의 역할을 설명한다
- [ ] shape 오류를 스스로 추적해 고친다
- [ ] self-attention 수식을 코드와 함께 설명한다
- [ ] 사전학습 모델에 LoRA를 붙여 학습하고 평가한다

## 자주 나오는 면접 질문

- 역전파는 PyTorch에서 어떻게 동작하나? (계산 그래프, autograd)
- Attention이 RNN보다 나은 점? 단점은? (O(n²))
- 학습이 안 될 때 점검 순서?
- LoRA/QLoRA는 무엇이고 언제 쓰나?
