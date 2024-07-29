(set-logic BV)

(define-fun hd17 ((x (_ BitVec 8))) (_ BitVec 8)
    (bvand (bvadd (bvor x (bvsub x #x01)) #x01) x))
(synth-fun f ((x (_ BitVec 8))) (_ BitVec 8)
    ((Start (_ BitVec 8)))
    ((Start (_ BitVec 8) ((bvnot Start) (bvxor Start Start) (bvand Start Start) (bvor Start Start) (bvneg Start) (bvadd Start Start) (bvmul Start Start) (bvudiv Start Start) (bvurem Start Start) (bvlshr Start Start) (bvashr Start Start) (bvshl Start Start) (bvsdiv Start Start) (bvsrem Start Start) (bvsub Start Start) x #x1F #x01 #x00 #xff))))

(declare-var x (_ BitVec 8))
(constraint (= (hd17 x) (f x)))

(check-synth)

