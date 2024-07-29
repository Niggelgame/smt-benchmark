(set-logic BV)

(define-fun hd06 ((x (_ BitVec 8))) (_ BitVec 8)
    (bvor x (bvadd x #x01)))
(synth-fun f ((x (_ BitVec 8))) (_ BitVec 8)
    ((Start (_ BitVec 8)))
    ((Start (_ BitVec 8) ((bvadd Start Start) (bvsub Start Start) (bvxor Start Start) (bvand Start Start) (bvneg Start) (bvor Start Start) #x00 #xff #x01 x))))

(declare-var x (_ BitVec 8))
(constraint (= (hd06 x) (f x)))

(check-synth)

