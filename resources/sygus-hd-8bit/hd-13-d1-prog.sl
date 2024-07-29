(set-logic BV)

(define-fun hd13 ((x (_ BitVec 8))) (_ BitVec 8)
    (bvor (bvashr x #x1F) (bvlshr (bvneg x) #x1F)))
(synth-fun f ((x (_ BitVec 8))) (_ BitVec 8)
    ((Start (_ BitVec 8)))
    ((Start (_ BitVec 8) ((bvlshr Start Start) (bvashr Start Start) (bvand Start Start) (bvxor Start Start) (bvor Start Start) (bvneg Start) (bvnot Start) (bvadd Start Start) (bvsub Start Start) x #x1F #x01 #x00 #xff))))

(declare-var x (_ BitVec 8))
(constraint (= (hd13 x) (f x)))

(check-synth)

