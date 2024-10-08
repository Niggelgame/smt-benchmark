(set-logic BV)

(define-fun hd02 ((x (_ BitVec 8))) (_ BitVec 8)
    (bvand x (bvadd x #x01)))
(synth-fun f ((x (_ BitVec 8))) (_ BitVec 8)
    ((Start (_ BitVec 8)))
    ((Start (_ BitVec 8) ((bvand Start Start) (bvsub Start Start) (bvor Start Start) (bvadd Start Start) (bvxor Start Start) x #x00 #xff #x01))))

(declare-var x (_ BitVec 8))
(constraint (= (hd02 x) (f x)))

(check-synth)

