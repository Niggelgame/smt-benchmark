(set-logic BV)

(define-fun hd13 ((x (_ BitVec 8))) (_ BitVec 8)
    (bvor (bvashr x #x1F) (bvlshr (bvneg x) #x1F)))
(synth-fun f ((x (_ BitVec 8))) (_ BitVec 8)
    ((Start (_ BitVec 8)))
    ((Start (_ BitVec 8) ((bvnot Start) (bvxor Start Start) (bvand Start Start) (bvor Start Start) (bvneg Start) (bvadd Start Start) (bvmul Start Start) (bvudiv Start Start) (bvurem Start Start) (bvlshr Start Start) (bvashr Start Start) (bvshl Start Start) (bvsdiv Start Start) (bvsrem Start Start) (bvsub Start Start) x #x1F #x01 #x00 #xff))))

(declare-var x (_ BitVec 8))
(constraint (= (hd13 x) (f x)))

(check-synth)

